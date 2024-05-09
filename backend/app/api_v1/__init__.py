from flask import Blueprint

api = Blueprint('api', __name__)



from . import analysis, blog, comment, post, product, reaction, sub, tag, user