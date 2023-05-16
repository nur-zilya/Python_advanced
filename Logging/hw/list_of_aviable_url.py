from flask import Flask

app = Flask(__name__)


@app.errorhandler(404)



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


if __name__ == "__main__":
    app.run(debug=True)