from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class CodeForm(FlaskForm):
    code = StringField('Code', validators=[InputRequired()])
    timeout = IntegerField('Timeout', validators=[InputRequired(), NumberRange(min=1, max=30)])

@app.route('/execute_code', methods=['POST'])
def execute_code():
    form = CodeForm(request.form)
    if form.validate():
        code = form.code.data
        timeout = form.timeout.data
        try:
            cmd = f'python -c "{code}"'
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out, err = process.communicate(timeout=timeout)
            if err:
                return jsonify({'error': err.decode('utf-8')})
            else:
                return jsonify({'output': out.decode('utf-8')})
        except subprocess.TimeoutExpired:
            return jsonify({'error': f'Timeout of {timeout} seconds exceeded.'})
    else:
        return jsonify({'error': 'Invalid input.'})

if __name__ == '__main__':
    app.run(debug=True)
