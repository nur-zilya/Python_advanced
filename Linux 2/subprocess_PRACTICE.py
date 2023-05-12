import shlex
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def return_ip():
    command = 'curl -i -H "Accept: application/json" -X GET https://api.ipify.org?format=json'
    args = shlex.split(command)
    result = subprocess.run(args, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return output
