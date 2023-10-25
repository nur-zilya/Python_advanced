import shlex
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/ps')
def ps():
    args = request.args.getlist('arg')
    arg = ''.join(args)
    cmd = f'ps {arg}'
    command = shlex.split(cmd)
    result = subprocess.run(command, capture_output=True, text=True)

    return f"<pre>{result.stdout}<pre/>"

if __name__ == "__main__":
    app.run(debug=True)
