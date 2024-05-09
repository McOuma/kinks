from flask import  jsonify
from . import api


@api.route('/user', methods=["GET"])
def get_users():
    return "<h1>Welcome</h1>"