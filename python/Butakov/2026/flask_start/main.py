import random
import re
import os

from flask import Flask
from random import choice
from datetime import datetime, timedelta

app = Flask(__name__)

cars_list = ["Chevrolet", "Renault", "Ford", "Lada"]
cat_breeds = [
    "корниш-рекс",
    "русская голубая",
    "шотландская вислоухая",
    "мейн-кун",
    "манчкин"
]

@app.route('/')
def base():
    return 'Для корня не было задания :('

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/cars')
def get_cars():
    return ", ".join(cars_list)

@app.route('/cats')
def get_random_cat():
    return choice(cat_breeds)

@app.route('/get_time/now')
def get_current_time():
    current_time = datetime.now()
    return f"Точное время: {current_time}"

@app.route('/get_time/future')
def future_time():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    time_str = current_time_after_hour.strftime('%H:%M:%S')
    return f'Точное время через час будет {time_str}'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

_words_list = None

def get_words_from_book():
    global _words_list
    if _words_list is not None:
        return _words_list
    
    with open(BOOK_FILE, 'r', encoding='utf-8') as book:
        text = book.read()
    
    words = re.findall(r'[а-яА-Яa-zA-Z]+', text)
    _words_list = words
    return words

@app.route('/get_random_word')
def random_word():
    words = get_words_from_book()
    if not words:
        return 'Ошибка: не удалось прочитать слова из книги'
    word = random.choice(words)
    return word

visits = 0

@app.route('/counter')
def counter():
    global visits
    visits += 1
    return f"Страница открыта {visits} раз"

if __name__ == '__main__':
    app.run(debug=True)