import os
from flask import Flask


app = Flask(__name__)


@app.route("/preview/<int:size>/<path:relative_path>")
def preview(size: int, relative_path):
    abs_path = os.path.abspath(relative_path)
    print(abs_path)
    with open(abs_path, 'r', encoding='utf-8') as f:
        result = f.read(size)
    return f"<b>{abs_path}</b> {size} <br>{result}"



if __name__ == "__main__":
    app.run(debug=True)
