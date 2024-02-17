from flask import Flask, render_template, make_response, request as req, jsonify
from os import walk, getcwd, path

fouder = 'templates/courses'

basepath = getcwd()

app = Flask(__name__)

@app.route('/', methods=('POST','GET'))
def index():
    return render_template('index.html')

@app.route('/center/', methods=('POST','GET'))
def center():
    quests = walk(path.join(basepath,fouder))
    data = {
        'topic':[],
    }
    for quest in quests:
        if quest[1]:
            data['topic'] = quest[1]
            for topic in quest[1]:
                data[topic] = []
        elif quest[2]:
            for content in quest[2]:
                data[quest[0].split('\\')[-1]].append(content.split('.html')[0])
    return jsonify(data)

@app.route('/<topic>/<content>/')
def quest(topic='',content=''):
    try:
        way = f'/courses/{topic}/{content}.html'
        return render_template(way)
    except Exception as erro:
        print(erro)
        return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
