from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")

@app.route("/teste")
def inoa():
    return render_template("site/index.html")

@app.route("/nothing-secret")
def nothing_secret():
    return "Nothing secret here!"


