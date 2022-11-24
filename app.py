from flask import Flask, render_template

from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(20, 20)
    GameOfLife.counter = 0
    return render_template('index.html')


@app.route('/live')
def live():
    new_live = GameOfLife()
    if new_live.counter > 0:
        new_live.form_new_generation()
    new_live.counter += 1
    return render_template('live.html', live=new_live)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
