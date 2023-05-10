import shlex
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/ps')
def ps():
    args = request.args.getlist('arg')
    cmd = ['ps'] + args
    clean_cmd = [shlex.quote(arg) for arg in cmd]
    result = subprocess.run(clean_cmd, capture_output=True, text=True)
    return f"<pre>{result.stdout}</pre>"


if __name__ == "__main__":
    app.run(debug=True)