from flask import Flask, request
import subprocess


app = Flask(__name__)

@app.route('/ps<args>', methods=['GET'])
def get_args(*args):
     arguments = request.args.getlist('arg')
     user_cmd = subprocess.check_output(arguments).decode('utf-8').strip("")
     print(user_cmd)