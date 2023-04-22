from flask import Flask
from datetime import datetime


weekday = datetime.today().weekday()


app = Flask(__name__)

@app.route('/hello_world/<name>')
def hello(name):
    tuple_weekdays = ('Понедельника', 'Вторника', 'Среды', 'Четверга', 'Пятницы', 'Субботы', 'Воскресенья')
    if weekday == 2 or weekday == 4 or weekday == 5:
        return f'Привет, {name}. Хорошей {tuple_weekdays[weekday]}!'
    else:
        return f'Привет, {name}. Хорошего {tuple_weekdays[weekday]}!'

if __name__ == "__main__":
    app.run(debug=True)



