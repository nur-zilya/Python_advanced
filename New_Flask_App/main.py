import datetime
from datetime import timedelta
from flask import Flask
import random
import os


app = Flask(__name__)

count = 0
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, '../Linux_base/text/war_and_peace.txt')


@app.route('/hello_world')
def print_hello():
    return "Hello, world!"


@app.route('/cars')
def cars():
    return "Chevrolet, Renault, Ford, Lada"


@app.route('/cats')
def cats():
    cats_list = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
    return random.choice(cats_list)


@app.route('/get_time/now')
def time_now():
    return "Точное время: {0}".format(datetime.datetime.now())


@app.route('/get_time/future')
def time_future():
    time = datetime.datetime.now() + timedelta(hours=1)
    return "Точное время через час будет {0}".format(time)


@app.route('/get_random_word')
def random_word():
    global lines
    if len(lines) == 0:
        with open(BOOK_FILE, "r", encoding="UTF-8") as war_and_peace:
            for line in war_and_peace.readlines():
                for item in line.split():
                    lines.append(item)
    return random.choice(lines)


lines = []


@app.route('/counter')
def counter_func():
    global count
    count += 1
    return "Текущая страница открывалась: {} раз".format(count)


if __name__ == "__main__":
    app.run(debug=True)
