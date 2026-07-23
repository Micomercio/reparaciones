from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/endesarrollo")
def endesarrollo():
    return render_template("endesarrollo.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)