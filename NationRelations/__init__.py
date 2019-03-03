from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/daniel")
def daniel():
    return "Daniel loves flask with all his heart"

if __name__ == "__main__":
    app.run(debug=True)
