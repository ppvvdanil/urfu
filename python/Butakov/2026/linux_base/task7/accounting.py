from flask import Flask

app = Flask(__name__)

year_totals: dict[int, int] = {}
month_totals: dict[tuple[int, int], int] = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int) -> str:
    year = int(date[:4])
    month = int(date[4:6])

    year_totals[year] = year_totals.get(year, 0) + number
    month_key = (year, month)
    month_totals[month_key] = month_totals.get(month_key, 0) + number

    return f"Добавлено: {number} руб. на дату {date}"


@app.route("/calculate/<int:year>")
def calculate_year(year: int) -> str:
    return str(year_totals.get(year, 0))


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int) -> str:
    if month < 1 or month > 12:
        return "Ошибка: месяц должен быть в диапазоне от 1 до 12"
    return str(month_totals.get((year, month), 0))


if __name__ == "__main__":
    app.run(debug=True)
