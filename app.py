from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("haruhito.html")

app.run(host="0.0.0.0")