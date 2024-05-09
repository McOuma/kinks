from flask import request
from app.model import User
from app.schema import UserSchem
from . import api


@api.route('/user', methods=["GET"])
def get_users():
    return "<h1>Welcome</h1>"


@api.route('/users', methods=["Get"])
def get_users():
    users = User.query.all()
    schema = UserSchem(many=True)
    return {schema.dump(users)}, 201


@api.route("/register", methods=["POST"])
def register():
    schema = UserSchem()
    data = schema.load(request.json)
    user = User.get_username(username)