import random
from flask import Flask, request, jsonify
from celery import Celery, group, beat
import time
from PIL import Image, ImageFilter
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'module_22_TaskQueue/hw/imgs'


def make_celery(app):
    celery = Celery(
       app.import_name
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
       def __call__(self, *args, **kwargs):
           with app.app_context():
               return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

app = Flask(__name__)
app.config.update(
   CELERY_BROKER_URL='redis://localhost:6379/0',
   CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)
celery = make_celery(app)

recepients = []

app.config.beat_schedule = {
   'send-email-every-week': {
       'task': 'tasks.send_email',
       'schedule': 604800.0, # 1 week in seconds
       'args': (recepients,)
   },
}

@celery.task(bind=True)
def process_image(self, image_path:str):
    with Image.open(image_path) as img:
        img.load()
    blur_img = img.filter(ImageFilter.BLUR)
    blur_img.save(f'{image_path}_blurred.jpg')

    time.sleep(random.randint(5, 15))
    #processed
    self.update_state(state='STARTED')
    # mocking email sending
    subscribe_by_email()
    # time.sleep(random.randint(1, 5))
    #email sended
    self.update_state(state='SUCCESS')

@app.route('/blur', methods=['POST'])
def process_images():
  images = request.files.getlist('images')

  if images and isinstance(images, list):
      image_paths = []
      for image in images:
          filename = secure_filename(image.filename)
          image_path = os.path.join(UPLOAD_FOLDER, filename)
          image.save(image_path)
          image_paths.append(image_path)

      # Создаём группу задач
      task_group = group(
          process_image.s(image_path)
          for image_path in image_paths
      )

      # Запускаем группу задач и сохраняем её
      result = task_group.apply_async()
      result.save()

      # Возвращаем пользователю ID группы для отслеживания
      return jsonify({'group_id': result.id}), 202
  else:
      return jsonify({'error': 'Missing or invalid images parameter'}), 400



@app.route('/status/<group_id>', methods=['GET'])
def get_group_status(group_id: str):
    result = celery.GroupResult.restore(group_id)

    if result:
      # Если группа с таким ID существует,
      # возвращаем долю выполненных задач
      progress = result.completed_count() / len(result)
      if result.info == 'PENDING':
          response = {
              'state': result.state,
              'status': 'waiting',
              'progress': progress
          }
      elif result.info == 'STARTED':
          response = {
              'state': result.state,
              'status': 'processing',
              'progress': progress
          }
      elif result.info == 'SUCCESS':
          response = {
              'state': result.state,
              'status': 'processed',
              'progress': progress
          }
      else:
          response = {
              'state': result.state,
              'status': 'failure'
          }
      return jsonify(response), 200
    else:
      # Иначе возвращаем ошибку
      return 404


@app.route('/subscribe', methods=['POST'])
def subscribe_by_email():
    email = request.form.get('email')
    if email:
        recepients.append(email)


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form.get('email')
    if email and email in recepients:
        recepients.remove(email)


if __name__ == "__main__":
    app.run(debug=True)
