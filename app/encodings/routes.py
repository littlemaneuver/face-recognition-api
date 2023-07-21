from flask import Blueprint
from flask import jsonify
from flask import request

from app.errors import InvalidAPIUsage

from . import repository
from . import service

encodings = Blueprint("encodings", __name__, url_prefix="/encodings")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


def allowed_file(filename):
    return (
        request.files["file"].filename != ""
        and "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@encodings.post("/")
def create_encoding():
    if "file" not in request.files:
        raise InvalidAPIUsage("no file part", status_code=400)

    image_file = request.files["file"]

    if not allowed_file(image_file.filename):
        raise InvalidAPIUsage("not allowed file", status_code=400)

    encoding = service.image_to_encoding(image_file)

    if encoding is None:
        raise InvalidAPIUsage("no face was found", status_code=400)

    inserted_encoding = repository.create(encoding.tolist())

    return inserted_encoding, 201


@encodings.get("/")
def get_all():
    return repository.query_all()


@encodings.get("/<id>")
def get_one(id):
    return repository.query_one(int(id, 10))


@encodings.get("/stats/count")
def get_count():
    return jsonify({"count": repository.count()})


@encodings.get("/stats/mean-encoding")
def get_mean_encoding():
    return jsonify({"mean_encoding": repository.mean_encoding()})
