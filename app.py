from flask import Flask

app = Flask(__name__)

@app.route("/")
def top():
    return "Haruhito"

app.run(host="0.0.0.0")