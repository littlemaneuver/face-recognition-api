"""init

Revision ID: 1_init
Revises:
Create Date:

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2023_07_21_base"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "face_encodings",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
            primary_key=True,
            autoincrement=True,
        ),
        sa.Column(
            "encoding", sa.ARRAY(sa.Float(precision=28)), nullable=False
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
    )


def downgrade():
    op.drop_table("face_encodings")
