import random

from flask import Flask, request, jsonify
from celery import Celery, group
import time
from threading import Thread

app = Flask(__name__)

celery = Celery(
   app.name,
   broker='redis://localhost:6379/0',
   backend='redis://localhost:6379/0',
)

# Задача Celery для обработки изображения
@celery.task
def process_image(image_id: str):
   # В реальной ситуации здесь может быть обработка изображения
   # В данном примере просто делаем задержку для демонстрации
   time.sleep(random.randint(5, 15))
   return f'Image {image_id} processed'

@app.route('/process_images', methods=['POST'])
def process_images():
   images = request.json.get('images')

   if images and isinstance(images, list):
       # Создаём группу задач
       task_group = group(
           process_image.s(image_id)
           for image_id in images
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
       status = result.completed_count() / len(result)
       return jsonify({'status': status}), 200
   else:
       # Иначе возвращаем ошибку
       return jsonify({'error': 'Invalid group_id'}), 404

@app.route('/cancel/<group_id>', methods=['POST'])
def cancel_group(group_id: str):
    result = celery.control.revoke(group_id, terminate=True)

    if result:
        return jsonify({'status': 'Cancelled'}), 200
    else:
        # Иначе возвращаем ошибку
        return jsonify({'error': 'Invalid group_id'}), 404

should_continue = True


def refresh_info():
   while should_continue:
       time.sleep(10)

Thread(target=refresh_info).start()

@app.route('/control', methods=['GET'])
def control():
    i = celery.control.inspect()

     # Get the list of active tasks
    active_tasks = i.active()

     # Convert the active tasks to a dictionary
    info = {'active_tasks': active_tasks}

    return jsonify(info)


@app.route('/stop', methods=['POST'])
def stop_refresh():
   global should_continue
   should_continue = False
   return jsonify({'status': 'Stopping refresh'})

if __name__ == '__main__':
   app.run(debug=True)