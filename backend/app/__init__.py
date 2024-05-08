from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """function to create the app instance"""
    app = Flask(__name__)
    app.config.from_object('config.Development')
    db.init_app(app)
    return app
