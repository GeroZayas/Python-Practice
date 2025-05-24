from flask import Flask, render_template, url_for

app = Flask(
    __name__,
)


@app.route("/")
def home():
    return "Hello, This is home"


@app.route("/index")
def index():
    return render_template("./index.html")


url_for("testing")

if __name__ == "__main__":
    app.run(debug=True)
