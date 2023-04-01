from flask import Blueprint, render_template

api = Blueprint("oddash_monty", __name__)


@api.route("/", methods=["GET"])
def watcher():
    return render_template("monty/dashboard.html")
