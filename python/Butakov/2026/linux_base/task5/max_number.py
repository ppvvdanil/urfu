from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers_path>")
def max_number(numbers_path: str) -> str:
    parts = [part for part in numbers_path.split("/") if part != ""]
    if not parts:
        return "Ошибка: не переданы числа"

    numbers: list[int] = []
    for part in parts:
        try:
            numbers.append(int(part))
        except ValueError:
            return f"Ошибка: '{part}' не является числом"

    max_value = max(numbers)
    return f"Максимальное переданное число <i>{max_value}</i>"


if __name__ == "__main__":
    app.run(debug=True)
