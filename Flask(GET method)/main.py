import flask 
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')



@app.route('/index/')
def index():
    if 's' and 'd' in request.args:
        s = request.args['s']
        d = request.args['d']
        return render_template('index.html', s=s, d=d)
        

if __name__ == '__main__':
    app.run(debug=True)