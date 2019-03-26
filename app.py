from flask import Flask, render_template, url_for
from api_consumer import get_people
from random import randint


app = Flask(__name__)

@app.route('/')
def index():
    dict_people = get_people()
    correct_answer = int(dict_people['height'])
    wrong_alternatives = [correct_answer - 15, correct_answer + 15, correct_answer + 30, correct_answer - 30]
    return render_template('index.html', dict_people=dict_people, secret_pos_correct=randint(0,3), wrong_alternatives=wrong_alternatives)


@app.route('/right')
def right():
    return render_template('right.html')
    
@app.route('/wrong/<correct>-<name>')
def wrong(correct, name):
    return render_template('wrong.html', correct=correct, name=name)


if __name__ == '__main__':
    app.run(debug=True)