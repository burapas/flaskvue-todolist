from flask import render_template, redirect, url_for, Blueprint


main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")