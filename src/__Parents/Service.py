import base64
from datetime import time
import datetime
from flask import make_response, jsonify
import os
from src import app
from flask import request
from datetime import datetime
import random
import string


class Service:
    # RANDOM CODE
    @staticmethod
    def generate_random_code(length=40, uppercase=True, lowercase=True, numbers=True):
        ticket_code = ''

        if uppercase:
            ticket_code += string.ascii_uppercase
        if lowercase:
            ticket_code += string.ascii_lowercase
        if numbers:
            ticket_code += string.digits

        return ''.join(random.choice(ticket_code) for i in range(length))

    @staticmethod
    def get_encode_image(image_path: str, dir_path: str or None = None):
        # CONVERT TO BASE64 AND SEND RESPONSE
        with open(os.path.join(dir_path or app.config["IMAGE_UPLOADS"], image_path), 'rb') as binary_file:
            base64_encoded_data = base64.b64encode(binary_file.read())

            return {'format': image_path.split('.')[-1],
                    'b64': str(base64_encoded_data.decode('utf-8')),
                    'filename': image_path}

    @staticmethod
    def get_date_time(date_time):
        return date_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    @staticmethod
    def response(success, obj, status_code) -> make_response:
        return make_response(jsonify(success=success, obj=obj), status_code)

    # RESPONSES
    @staticmethod
    def response_conflict(msg=None):
        return Service.response(False, {'msg': msg or 'exist'}, 409)

    @staticmethod
    def response_not_found(msg=None):
        return Service.response(False, {'msg': msg or 'not found'}, 404)

    @staticmethod
    def response_invalid_password():
        return Service.response(False, {'msg': 'incorrect password'}, 403)

    @staticmethod
    def response_created(msg=None):
        return Service.response(True, {'msg': msg or 'successfully created'}, 201)

    @staticmethod
    def response_updated(msg=None):
        return Service.response(True, {'msg': msg or 'successfully updated'}, 200)

    @staticmethod
    def response_ok(obj):
        return Service.response(True, obj, 200)

    @staticmethod
    def response_deleted(msg=None):
        return Service.response(True, {'msg': msg or 'successfully deleted'}, 200)

    @staticmethod
    def response_invalid_login():
        return Service.response(False, {'msg': 'invalid username and/or password'}, 401)
