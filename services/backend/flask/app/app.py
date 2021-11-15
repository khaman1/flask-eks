from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/env")
def check_env():
    return "<p>Hello, World! Current environment: " + os.environ['CURRENT_ENV'] + "</p>"

from library.db.postgres.postgres import Postgres
@app.route("/account")
def get_account_public_information():
    return Postgres().get_account(account_id=1)