from flask import jsonify
from . import api
from app.exeption import ValidationError


@api.errorhandler(ValidationError)
def bad_request(e):
    response = jsonify({"status": 400, 'error': 'bad request', 'message': e.args[0]})
    response.status_code = 400
    return response


@api.errorhandler(404)
def not_found(e):
    response = jsonify({"status": 404, "error": "Not Found", "message": "Invalid Resource URI"})
    response.status_code = 404
    return response


@api.errorhandler(405)
def method_not_supported(e):
    response = jsonify({"status": 405, "error": "Method NOT Supported", "message":"The method is not supported"})
    response.status_code = 405
    return response


@api.errorhandler(503)
def internal_server_error(e):
    response = jsonify({"status": 503, "error": "Internal Server Error", "message": e.args[0]})
    response.status_code = 503
    return response