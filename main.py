from flask import Flask, render_template

app = Flask(__name__)

@app.route("/qwe") #decorator
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/firstpage")
def first_page():
    return render_template('100xcohort.html')