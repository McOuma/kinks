class Development:
    DEBUG = True
    SECRET_KEY = "topsecret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = True