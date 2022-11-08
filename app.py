from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

app.secret_key = "Exemple_key"


# localhost 5000
@app.route("/")
def init():
    if "username" in session:
        return f"User logged: {session['username']}"
    return "User not logged"

    # app.logger.debug("debug msg")  # Only debug mode
    # app.logger.info(f"Enter in {request.path}")  # Only debug mode
    # app.logger.warn("Warn msg")
    # app.logger.error("Error msg")
    # return "Hello world 3"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("init"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("init"))


@app.route("/welcome/<name>")
def welcome(name):
    return f"Welcome {name}"


@app.route("/age/<int:age>")
def years(age):
    return f"Your age is {age}"


@app.route("/show/<name>", methods=["POST", "GET"])  # Default method = GET
def show_name(name):
    return render_template("show.html", name=name)


@app.route("/redirect")
def redirection():
    return redirect(url_for("init"))


@app.route("/exit")
def exit():
    return abort(404)


@app.route("/api/show/<name>", methods=["GET", "POST"])
def show_api(name):
    return jsonify({"name": name, "method_request": request.method})


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error404.html", error=error), 404
