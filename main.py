from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/<username>")
def welcome(username):
    return render_template("index.html", name = username)

@app.route("/grade/<int:grade>")
def grade(grade):
    if grade >= 90:
        result = "A+"
    elif grade >= 85:
        result = "A"
    elif grade >= 80:
        result = "A-"
    elif grade >= 75:
        result = "B+"
    elif grade >= 70:
        result = "B"
    elif grade >= 70:
        result = "B-"
    
    return render_template("index.html", mark = result)


if __name__ == '__main__':
    app.run(debug = True, port = 8000)
