from flask import Flask
import subprocess

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    result = subprocess.run(["uptime", "-p"], capture_output=True, text=True)
    if result.returncode != 0:
        return "Ошибка получения времени", 500

    uptime_value = result.stdout.strip()
    return f"Время работы - {uptime_value}"


if __name__ == '__main__':
    app.run(debug=True)
