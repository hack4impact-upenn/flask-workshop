from flask import render_template
from app import app


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/<name>/<int:rating>", methods=['GET'])
def welcome(name, rating):
    return render_template('welcome.html', name=name, rating=rating)
