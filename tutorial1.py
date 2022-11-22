from flask import Flask, redirect, url_for

app = Flask(__name__)
adm = False


@app.route("/")
def home():
    return "<h1> Home Page <h1>"
    # can return in line HTML files
    # using this just as a placeholder for now


@app.route("/<name>")  # will actually print out the name that is passed
def user(name):
    return f"Hello {name}!"  # use this to print name out


@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    app.run()
