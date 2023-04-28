from flask import Flask

app = Flask(__name__)
expenses = {}


@app.route("/add/<date>/<int:number>")
def daily_expense(date, number):
    year = int(date[:4])
    if int(date[5]) >= 10:
        month = int(date[5:7])
        day = int(date[8:])
    else:
        month = int(date[4:5])
        day = int(date[5:])
    expenses.setdefault(year, {}).setdefault(month, {})[day] = number
    return f'Today {year}.{month}.{day} expenses are {expenses[year][month][day]}'

@app.route("/calculate/<int:year>")
def year_expenses(year):
    if int(year) not in expenses:
        return f"No expenses found for the year {year}"

    total_expenses = 0
    for month in expenses[year]:
        for day_expense in expenses[year][month].values():
            total_expenses += day_expense
    return f'Year {year} expenses are {total_expenses}'


@app.route('/calculate/<int:year>/<int:month>')
def month_expenses(year, month):
    total_expenses = sum(expenses.get(int(year), {}).get(int(month), {}).values())
    return f'Monthly expenses are {total_expenses}'

if __name__ == "__main__":
    app.run(debug=True)
