from flask import Flask, render_template, make_response
from os import listdir

fouder = 'quests/'

listdir()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<quest_name>')
def quest(quest_name=''):
    try:
        return render_template(fouder+f'{quest_name}.html')
    except:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')