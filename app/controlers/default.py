from app.__init__ import app, render_template, jsonify, make_response, req
from app.models import models
import os
import hashlib

def error(text=''):
    return f'\033[31;3m{text}\033[;m'

fouder = 'app/templates/courses'

admin_file_path = 'app/templates/admin_signed.html'

basepath = os.getcwd()

print(basepath)

data =  []

#data = os.environ['ADMIN'].split(',')

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
    elif (req.method == 'PUT'):
        pass
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

@app.route('/admin/', methods=('POST','GET','DELETE','PUT'))
def admin():
    if (req.method != 'GET'):
        mode = req.mimetype_params['mode']
        if req.is_json:
            json = req.json
            print(json)
            match (req.method):
                case 'POST':
                    models.center(mode,json)
                case 'DELETE':
                    models.center(mode,json)
                case 'PUT':
                    models.center(mode,json)
            return jsonify({'resp':'ok'})
    else: return render_template('admin_signed.html')

#@app.route('/admin', methods=('POST','GET'))
#def admin():
#    if req.method == 'POST':
#        resp = ''
#        if req.is_json:
#            resp = req.json
#        print(req.json)
#        password = hash(resp['password'])
#        if data[0] == resp['username'] and data[1] == password:
#            content = {'resp':''}
#            with open(os.path.join(basepath,admin_file_path), 'r') as f:
#                content['resp'] = f.read()
#                f.close()
#            return jsonify(content)
#        else: return jsonify({'resp':'username or password incorrect'})
#    return render_template('admin.html')
