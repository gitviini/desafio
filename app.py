from flask import Flask, render_template, make_response, request as req, jsonify
import json
import os
import hashlib

def error(text=''):
    return f'\033[31;3m{text}\033[;m'

fouder = 'templates/courses'

admin_file_path = 'templates/admin_signed.html'

basepath = os.getcwd()

data = os.environ['ADMIN'].split(',')

app = Flask(__name__)

#util

def hash(text='') -> str:
    text = text.encode('utf-8')
    sha = hashlib.sha256()
    sha.update(text)
    return sha.hexdigest()

#manager admin
def admin_center(req='') -> any:
    if (req.method == 'POST'):
        mode = req.mimetype_params['mode']
        print(mode)
        match (mode):
            case 'admin_signed':
                if req.is_json:
                    resp = req.json
                    password = hash(resp['password'])
                    if data[0] == resp['username'] and data[1] == password:
                        content = {
                            'headers':{
                                'Content-Type':'application/json',
                            },
                            'resp':''
                            }
                        with open(os.path.join(basepath,admin_file_path), 'r') as f:
                            content['resp'] = f.read()
                            f.close()
                        return jsonify(content)
                    else: return jsonify({'resp':'username or password incorrect'})
            case 2:
                pass
            case _:
                print(error(f'admin_center:. not found {mode}'))
    if (req.method == 'GET'):
        return render_template('admin.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/center/')
def center():
    quests = os.walk(os.path.join(basepath,fouder))
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
                if os.name == 'nt':
                    data[quest[0].split('\\')[-1]].append(content.split('.html')[0])
                elif os.name =='posix':
                    data[quest[0].split('/')[-1]].append(content.split('.html')[0])
                else: print(os.name)
    return jsonify(data)

@app.route('/<topic>/<content>/')
def quest(topic='',content=''):
    try:
        way = f'/courses/{topic}/{content}.html'
        return render_template(way)
    except Exception as erro:
        print(erro)
        return render_template('error.html')

@app.route('/admin', methods=['POST','GET','DELETE','PUT'])
def admin():
    return admin_center(req)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')