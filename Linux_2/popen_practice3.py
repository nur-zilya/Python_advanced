import subprocess
import time

# запускаем команду в фоновом режиме
process = subprocess.Popen(['sleep', '10', '&&', 'exit', '1'])

# ждем 9 секунд
time.sleep(3)

# проверяем, что процесс не завершен
if process.poll() is None:
    print("Process is still running")

# ждем, пока команда завершится
return_code = process.wait(timeout=1)

# выводим код возврата
print(f"Command exited with return code: {return_code}")
