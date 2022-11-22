from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
    # now instead of inline HTML we are rendering an HTML file


if __name__ == "__main__":
    app.run()
