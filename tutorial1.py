from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    # we can have it send name as a parameter to the index.html file
    return render_template("index.html")
    # now instead of inline HTML we are rendering an HTML file


if __name__ == "__main__":
    app.run()
