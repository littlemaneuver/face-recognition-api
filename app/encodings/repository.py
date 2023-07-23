import numpy as np
from sqlalchemy import select

from app.extensions import db

from .model import FaceEncoding


def query_all():
    all = []
    for row in db.session.execute(select(FaceEncoding)):
        all.append(
            {
                "id": row.FaceEncoding.id,
                "encoding": row.FaceEncoding.encoding,
            }
        )

    return all


def query_one(id):
    stmt = select(FaceEncoding).where(FaceEncoding.id == id)
    row = db.session.execute(stmt).fetchone()

    if row is None:
        return None

    return {
        "id": row.FaceEncoding.id,
        "encoding": row.FaceEncoding.encoding,
    }


def create(encoding):
    face_encoding = FaceEncoding(encoding=encoding)
    db.session.add(face_encoding)
    db.session.commit()
    db.session.refresh(face_encoding)
    return {
        "id": face_encoding.id,
        "encoding": face_encoding.encoding,
    }


def count():
    return db.session.query(FaceEncoding.id).count()


def mean_encoding():
    all_encodings = list(map(lambda x: x["encoding"], query_all()))
    return np.mean(all_encodings, axis=0).tolist()
