from flask import request
from . import api
from app.schema import CommentSchema
from app import db
from app.model import Comment


@api.route('/comment', methods=["POST"])
def new_comment():
    schema = CommentSchema()
    data = schema.load(request.json)
    comment = Comment(**data)
    db.session.add(comment)
    db.session.commit()
    return {schema.dump(comment)}, 201


@api.route('/comment', methods=["GET"])
def get_comments():
    schema = CommentSchema(many=True)
    comment = Comment.query.all()
    return {schema.dump(comment)}, 200


@api.route('/comment/<int:id>', methods=["GET"])
def get_comment(id):
    schema = CommentSchema()
    comment = Comment.query.get_or_404(id)
    return {schema.dump(comment)}, 200


@api.route('/comment/<int:id>', methods=["PUT"])
def edit_comment(id):
    schema = CommentSchema(partial=True)
    comment = Comment.query.get_or_404(id)
    comment = schema.load(request.json, instance=comment)
    db.session.add(comment)
    db.session.commit()
    return {schema.dump(comment)}, 201


@api.route('/comment/<int:id>', methods=["DELETE"])
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return {"message": "Comment Deleted"}, 201