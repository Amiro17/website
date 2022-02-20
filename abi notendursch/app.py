from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home1.html")


@app.route("/", methods=["POST"])
def my_form_post():
    text1 = request.form["choice1"]
    text2 = request.form["choice2"]
    text3 = request.form["choice3"]
    print(text1, text2, text3)
    return ("", 204)


@app.route("/Amiro")
def my_link():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
