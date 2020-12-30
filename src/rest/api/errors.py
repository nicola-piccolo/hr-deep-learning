from flask import jsonify, make_response
from . import mlEnvironmentTemplate

@mlEnvironmentTemplate.errorhandler(400)
def bad_request_handler():
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@mlEnvironmentTemplate.app_errorhandler(404)
def not_found_handler(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@mlEnvironmentTemplate.errorhandler(500)
def internal_server_error_handler():
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)