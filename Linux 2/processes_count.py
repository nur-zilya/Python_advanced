import subprocess

command = "ps -A | wc -l"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
output = result.stdout.strip()

if output:
    num_processes = int(output)
    print(f'Number of processes running: {num_processes}')
else:
    print('No processes running')
