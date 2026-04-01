import os

from flask import Flask

app = Flask(__name__)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@app.route("/preview/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str) -> str:
    if size < 0:
        return "Ошибка: SIZE должен быть неотрицательным"

    absolute_path = os.path.abspath(os.path.join(PROJECT_ROOT, relative_path))

    try:
        with open(absolute_path, encoding="utf-8") as file:
            text = file.read(size)
    except OSError as error:
        return f"Ошибка чтения файла: {error}"

    return f"<b>{absolute_path}</b> {len(text)}<br>{text}"


if __name__ == "__main__":
    app.run(debug=True)
