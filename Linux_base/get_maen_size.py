import os
import sys

lines = sys.stdin.read()

def get_mean_size(lines):
    total_size = 0
    files_num = 0
    for line in lines.splitlines():
        # строки, начинающиеся с символа "-", что означает, что это файл (или символическая ссылка на файл)
       if line.startswith('-'):
            parts = line.split()
            total_size += int(parts[4])
            files_num += 1
    if files_num > 0:
        mean_size = total_size / files_num
        print(mean_size)


if __name__ == "__main__":
    get_mean_size(lines)


# import os
# import sys
#
# lines = sys.stdin.read()
#
# def get_mean_size(lines):
#     total_size = 0
#     file_count = 0
#     for line in lines.splitlines():
#         if line.startswith('-'):
#             parts = line.split()
#             total_size += int(parts[4])
#             file_count += 1
#     if file_count > 0:
#         mean_size = total_size / file_count
#         print(mean_size)
#
# if __name__ == "__main__":
#     get_mean_size(lines)
