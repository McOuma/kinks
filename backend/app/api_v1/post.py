from flask import request
from app.schema import PostSchema
from app.model import Post
from app import db
from . import api


@api.route('/post', methods=['POST'])
def new_post():
    schema = PostSchema()
    data = schema.load(request.json)
    post = Post(**data)
    db.session.add(post)
    db.session.commit()
    return {"message": "post created", "post": schema.dump(post)}, 201


@api.route('/post', methods=['GET'])
def get_posts():
    schema = PostSchema(many=True)
    posts = Post.query.all()
    return {schema.dump(posts)}, 200


@api.route('/post/<int:id>', methods=["GET"])
def get_post(id):
    schema = PostSchema()
    post = Post.get_404(id)
    return {schema.dump(post)}, 200


@api.route('/post/<int:id>', methods=["PUT"])
def edit_post(id):
    schema = PostSchema()
    post = Post.get_404(id)
    db.session.add(post)
    db.session.commit()
    return {schema.dump(post)}, 201


@api.route('/post/<int:id>', methods=["DELETE"])
def delete_post(id):
    schema = PostSchema()
    post = Post.get_404(id)
    db.session.delete(post)
    db.session.commit()
    return {"message": "post deleted"}, 200

