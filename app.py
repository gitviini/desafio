from flask import Flask, render_template, make_response, request as req, jsonify
from os import listdir, getcwd, path

fouder = 'templates/quests'

basepath = getcwd()

app = Flask(__name__)

@app.route('/', methods=('POST','GET'))
def index():
    return render_template('index.html')

@app.route('/center', methods=('POST','GET'))
def center():
    quests = listdir(path.join(basepath,fouder))
    data = []
    for quest in quests:
        data.append(quest.split('.html')[0])
    return jsonify(data)

@app.route('/<quest_name>')
def quest(quest_name=''):
    try:
        return render_template('/quests/'+f'{quest_name}.html')
    except:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
