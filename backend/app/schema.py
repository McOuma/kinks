from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String,Integer
from app import ma
from model import User, Post, Comment, Reaction, Tag, Subscription, Analytics


class UserSchema(ma.SQLAlchemyAutoSchema):
    username = String(required=True, validate=[validate.Length(min=4)])
    email = String(required=True, validate=[validate.Email])

    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get("email")
        if User.query.filter_by(email=email).count():
            raise ValidationError("Email {email} already exist.")

    class Meta:
        model = User
        load_instance = True
        exclude = ['id', 'password_hash']


class PostSchema(ma.SQLAlchemyAutoSchema):
    title = String(required=True, validate=[validate.Length(min=4)])
    content = String(required=True, validate=[validate.Length(min=10)])
    class Meta:
        model = Post
        load_instance = True
        exclude = ['id','author_id']


class CommentSchema(ma.SQLAlchemyAutoSchema):
    text = String(required=True, validate=[validate.Length(max=150)])
    class Meta:
        model = Comment
        load_instance = True
        exclude = ['id', 'post_id','parent_comment_id', 'user_id']


class ReactionSchema(ma.SQLAlchemyAutoSchema):
    reaction_type = String(required=True, validate=[validate.Length()])
    class Meta:
        model = Reaction
        load_instance = True
        exclude = ['id', 'post_id', 'user_id']


class TagSchema(ma.SQLAlchemyAutoSchema):
    name = String(required=True, validate=[validate.Length(min=4)])
    description = String(required=True, validate=[validate.Length(min=4)])
    class Meta:
        model = Tag
        exclude = ['id']
        load_instance = True


class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    first_name = String(required=True, validate=[validate.Length(min=3)])
    last_name = String(required=True, validate=[validate.Length(min=3)])
    email = String(required=True, validate=[validate.Email])
    class Meta:
        model = Subscription
        exclude = ['id']
        load_instance = True


class AnalyticsSchema(ma.SQLAlchemyAutoSchema):
    page_views = Integer()
    unique_visitors = Integer()
    class Meta:
        model = Analytics
        exclude = ['id', 'post_id']
        load_instance = True