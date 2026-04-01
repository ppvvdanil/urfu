from flask import Flask
from datetime import datetime
import sys

app = Flask(__name__)

WEEKDAYS = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')


@app.route('/hello-world/<name>')
def hello_world(name):
    weekday = datetime.today().weekday()  # 0 = понедельник, 6 = воскресенье
    day_name = WEEKDAYS[weekday]
    if day_name[-1] == "а": 
        good_word = "Хорошего" 
    else:
        good_word = "Хорошей" 
    return f'Привет, {name}. {good_word} {day_name}!'


if __name__ == '__main__':
    app.run()