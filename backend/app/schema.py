from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String
from app import ma
from model import User, Post


class UserSchema(ma.SQLAlchemyAutoSchema):
    username = String(required=True, validate=[validate.length(min=4)])
    email = String(required=True, validate=[validate.Email])

    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get("email")
        if User.query.filter_by(email=email).count():
            raise ValidationError("Email {email} already exist.")

    class Meta:
        model = User
        exclude = ['id', 'password_hash']


class PostSchema(ma.SQLAlchemyAutoSchema):
    title = String(required=True, validate=[validate.length(min=4)])
    content = String(required=True, validate=[validate.length(min=10)])
    class Meta:
        model = Post
        exclude = ['id','author_id']


