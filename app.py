from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from database import Person

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("haruhito.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/create", methods={"POST"})
def create():
    Person.create(
        name=request.form["name"],
        emotion=request.form["emotion"],
        age=request.form["age"],
    )
    return redirect("/")
app.run(host="0.0.0.0", debug=True)
