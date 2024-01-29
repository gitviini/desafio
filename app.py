from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('desafio1.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == "__main__":
    app.run(debug=True)