# pip install -r requirements.txt > naredba za inst

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    poruka = "Ovo je string iz main.py"

    gradovi = ["Zagreb", "Rijeka", "Split"]

    return render_template("index.html", poruka=poruka, gradovi=gradovi)

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run(use_reloader=True)