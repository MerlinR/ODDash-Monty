import requests
from flask import Blueprint, render_template, request

api = Blueprint("oddash_monty", __name__)

ENDPOINT_URL = "http://lxc-controller-01.lan:8000"


@api.route("/", methods=["GET"])
def dashboard():
    return render_template("monty/dashboard.html")


@api.route("/api", methods=["GET", "POST"])
def apideck():
    extra = {"msg": "", "type": ""}

    if request.method == "POST":
        action = request.form.get("action")
        extra["msg"] = action
        extra["type"] = "info"

        try:
            resp = requests.get(f"{ENDPOINT_URL}/{action}")

            extra["msg"] = resp.content.decode()

            if resp.status_code >= 200 and resp.status_code <= 300:
                if extra["msg"]:
                    extra["type"] = "info"
                else:
                    extra["type"] = "positive"
            else:
                extra["type"] = "error"

        except Exception as e:
            print(f"ERROR: {e}")
            extra["msg"] = e
            extra["type"] = "error"

    return render_template(
        "monty/apideck.html",
        msg=extra["msg"],
        msg_type=extra["type"],
    )
