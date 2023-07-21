import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FaceEncoding(Base):
    __tablename__ = "face_encodings"
    id = sa.Column(sa.Integer, primary_key=True)
    encoding = sa.Column(sa.ARRAY(sa.Float(precision=28)), nullable=False)

    def __repr__(self):
        return "<FaceEncoding(encoding='%s')>" % (self.encoding,)
