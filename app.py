import sys
import time
import random
from uuid import uuid4
from flask import Flask
from flask import request, jsonify, make_response
import logging
from custom_users import get_last_users

logger = logging.getLogger(name="SERVER")
formatter = logging.Formatter("%(asctime)s %(name)s: %(levelname)s - %(message)s")
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)

app = Flask(__name__)
users = get_last_users(count=100)
app.config["users"] = users
logger.info("Application init complete")
logger.info(f"last 10 users: {users[:10]}")

ACTIONS = [
    "CREATE NEW ORDER",
    "DELIVERED ORDER",
    "ADD CHANGES TO ORDER",
    "CANCEL ORDER",
    "CANCELLED EXPIRED ORDER",
    "PAYED FOR ORDER"
]


@app.route("/health", methods=["GET"])
def hello_world():
    logger.info("/health - OK")
    return make_response(
        jsonify({"status": "OK"}),
        200
    )


@app.route("/login", methods=["GET"])
def login(user):
    users = app.config["users"]
    if user in set(users):
        logger.info(f"SUCCESS LOGIN by {user}")
        return make_response(
            jsonify({"message": f"Login success {user}"}),
            200
        )
    return make_response(
        jsonify({"error": "Incorrect username or user doesnt exists"}),
        400
    )


@app.route("/order_test", methods=["GET"])
def login_test():
    users = app.config["users"]
    id = random.randint(0, len(users) - 1)
    user = users[id]
    action_id = random.randint(0, len(ACTIONS)-1)
    action = ACTIONS[action_id]
    order_id = str(uuid4())
    logger.info(f"SUCCESS LOGIN by {user}")
    time.sleep(3)
    logger.info(f"{user} - action - {action} - order - {order_id}")

    return make_response(
            jsonify({"status": "OK"}),
            200
        )


@app.route("/users", methods=["GET", "POST"])
def users():
    users = app.config["users"]
    if request.method == "GET":
        return make_response(
            jsonify(users),
            200
        )
    elif request.method == "POST":
        data = request.json
        logger.info(f"/users - try user: {data}")
        username = data.get("user")
        arr = username.split(" ")
        if len(arr) != 2:
            return make_response(
                jsonify({"error": "Incorrect user name. User must have name and lastname"}),
                400
            )
        users.append(username)
        return make_response(
                jsonify(users),
                201
            )

if __name__ == "__main__":
    app.run()
