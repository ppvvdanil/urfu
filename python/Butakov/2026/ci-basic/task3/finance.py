from datetime import datetime

from flask import Flask

app = Flask(__name__)

storage: dict[str, list[int]] = {}


def add(date: str, amount: int) -> None:
    datetime.strptime(date, "%Y%m%d")
    storage.setdefault(date, []).append(amount)


def calculate_year(year: int) -> int:
    year_prefix = f"{year:04d}"
    return sum(sum(amounts) for day, amounts in storage.items() if day.startswith(year_prefix))


def calculate_month(year: int, month: int) -> int:
    month_prefix = f"{year:04d}{month:02d}"
    return sum(sum(amounts) for day, amounts in storage.items() if day.startswith(month_prefix))


@app.route("/add/<date>/<int:number>")
def add_route(date: str, number: int) -> str:
    add(date, number)
    return "OK"


@app.route("/calculate/<int:year>")
def calculate_year_route(year: int) -> str:
    return str(calculate_year(year))


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month_route(year: int, month: int) -> str:
    return str(calculate_month(year, month))


if __name__ == "__main__":
    app.run(debug=True)
