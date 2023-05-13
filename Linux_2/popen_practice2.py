import subprocess
import time

start_time = time.time()

# создаем список процессов
processes = []
for i in range(10):
    process = subprocess.Popen(['sleep', '15', '&&', 'echo', f'My mission is done here! ({i})'])
    processes.append(process)

# ждем окончания всех процессов
for process in processes:
    process.wait()

end_time = time.time()

print(f"Total time taken: {end_time - start_time:.2f} seconds")
