from flask import Flask
from flask import json
from flask import jsonify

from app.encodings.routes import encodings
from app.errors import InvalidAPIUsage
from app.extensions import db


def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


def handle_known_exception(e):
    return jsonify(e.to_dict()), e.status_code


def create_app(settings_override=None):
    app = Flask(__name__)

    app.config.from_object("config.settings")

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(encodings)

    app.register_error_handler(500, handle_exception)
    app.register_error_handler(InvalidAPIUsage, handle_known_exception)

    extensions(app)

    return app


def extensions(app):
    db.init_app(app)

    return None
