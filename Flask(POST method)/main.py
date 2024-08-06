import flask
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        if 's' and 'd' in request.form:
            s = request.form["s"]
            d = request.form["d"]
            return render_template("index.html", s=s, d=d)            


if __name__ == "__main__":
    app.run(debug=True)