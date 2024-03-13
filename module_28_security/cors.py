from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello():
    print(request.headers)
    return f"Hello, world!"


@app.after_request
def add_cors(response: Response):
    response.headers['Access-Control-Allow-Origin'] = 'https://www.google.com'
    response.headers['Access-Control-Allow-Headers'] = 'X-My-Fancy-Header'
    response.headers['Access-Control-Allow-Methods'] = ['GET', 'POST']
    return response

if __name__ == "__main__":
    app.run(debug=True)