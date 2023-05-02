file_path = '/Users/hfast/Desktop/Python_advanced/Linux_basics/output_file.txt'


def get_summary_rss(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()[1:]  # пропускаем первую строку с заголовками
        rss_sum = sum(int(line.split()[5]) for line in lines)  # суммируем значения в пятом столбце
        # print(rss_sum)
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    unit_index = 0
    while rss_sum >= 1024 and unit_index < len(units) - 1:
        rss_sum /= 1024
        unit_index += 1
    print (f"{rss_sum:.2f} {units[unit_index]}")



if __name__ == "__main__":
    get_summary_rss(file_path)