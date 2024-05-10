from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String
from app import ma
from model import User, Post, Comment


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

#
# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
#     post = db.relationship('Post', backref=db.backref('comments', lazy=True))
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     author = db.relationship('User', backref=db.backref('comments', lazy=True))
#     text = db.Column(db.Text, nullable=False)
#     publication_date = db.Column(db.DateTime, nullable=False, default=db.func.now())


class CommentSchema(ma.SQLAlchemyAutoSchema):
    text = String(required=True, validate=[validate.length(max=150)])
    class Meta:
        model = Comment
        load_instance = True
        exclude = ['id', 'post-id', 'author_id']