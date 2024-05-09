from . import api


@api.route('/')
def get_home():
    return "<h1>Karibu from Post</h1>"