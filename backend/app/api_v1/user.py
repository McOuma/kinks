from flask import request
from app.model import User
from app.schema import UserSchema
from . import api
from app import db


@api.route('/user', methods=["GET"])
def get_users():
    return "<h1>Welcome</h1>"


@api.route('/users', methods=["Get"])
def get_users():
    users = User.query.all()
    schema = UserSchema(many=True)
    return {schema.dump(users)}, 200


@api.route("/register", methods=["POST"])
def register():
    schema = UserSchema()
    data = schema.load(request.json)
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return {"msg": "user created", 'user':schema.dump()}, 201


@api.route("/user/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = User.get_404(user_id)
    schema = UserSchema()
    return {schema.dump(user)}, 201

