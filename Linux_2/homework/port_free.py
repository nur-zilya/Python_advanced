import subprocess
import os
import time

def start_server(port):
    while True:
        try:
            command = f'python server.py {port}'
            subprocess.Popen(command, shell=True)
            print(f'Server started on port {port}')
            break 
        except:
            # если порт занят, находим процесс и завершаем его
            print(f'Port {port} is busy. Trying to kill the process...')
            command = f'lsof -i :{port}'
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
            if result.stdout:
                pid = result.stdout.split()[10]  # получаем PID процесса
                os.kill(int(pid), 9)  # завершаем процесс с указанным PID
                print(f'Process {pid} killed')
            time.sleep(1)  # ждем некоторое время перед следующей попыткой
