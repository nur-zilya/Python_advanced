from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/uptime', methods=['GET'])
def get_uptime():
    try:
        # Используем команду 'uptime' в терминале для получения времени работы системы
        uptime_result = subprocess.check_output(['uptime']).decode('utf-8').split(" ")
        res = uptime_result[4].rstrip(',')
        return f"Current uptime is {res}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run()
