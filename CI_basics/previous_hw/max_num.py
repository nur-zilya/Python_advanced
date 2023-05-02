from flask import Flask

app = Flask(__name__)

@app.route('/max_number/<path:numbers>')
def find_max_num(numbers):
    nums = numbers.split("/")
    max_num = float(nums[0])
    for num in nums:
        if not num.isdigit():
            return f'Ошибка: "{num}" не является числом'
        if float(num) > max_num:
            max_num = float(num)

    return f'Максимальное переданное число <i><b>{max_num}</b></i>'


if __name__ == "__main__":
    app.run(debug=True)
