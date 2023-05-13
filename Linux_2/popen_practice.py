import subprocess

# запускаем ps и отправляем результат в stdin wc -l
ps_process = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
wc_process = subprocess.Popen(['wc', '-l'], stdin=ps_process.stdout, stdout=subprocess.PIPE)

# получаем вывод от wc -l
output, _ = wc_process.communicate()

# конвертируем вывод в число
num_processes = int(output.strip())

print(f'Number of processes running: {num_processes}')
