from marshmallow import validate
from app import ma
from model import User


class UserSchem(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ['id', 'password_hash']

