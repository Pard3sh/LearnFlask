from flask import Flask, redirect, url_for

app = Flask(__name__)
adm = False


@app.route("/")
def home():
    return "<h1> Home Page <h1>"
    # can return in line HTML files
    # using this just as a placeholder for now


if __name__ == "__main__":
    app.run()
