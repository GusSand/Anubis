"""add-theia-options

Revision ID: 265635dac5b6
Revises: 0be9593348ba
Create Date: 2021-01-19 10:52:29.171727

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "265635dac5b6"
down_revision = "0be9593348ba"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    context = op.get_context()

    op.add_column(
        "assignment",
        sa.Column("theia_image", sa.String(length=128), nullable=True),
    )
    op.add_column(
        "theia_session",
        sa.Column("image", sa.String(length=128), nullable=True),
    )
    op.add_column(
        "theia_session",
        sa.Column("network_locked", sa.Boolean(), nullable=True),
    )
    op.add_column(
        "theia_session", sa.Column("options", sa.JSON(), nullable=False)
    )
    op.add_column(
        "theia_session", sa.Column("privileged", sa.Boolean(), nullable=True)
    )
    op.add_column(
        "theia_session",
        sa.Column("repo_url", sa.String(length=128), nullable=False),
    )
    op.alter_column(
        "theia_session",
        "assignment_id",
        existing_type=mysql.VARCHAR(length=128),
        nullable=True,
    )
    op.drop_constraint(
        "theia_session_ibfk_3", "theia_session", type_="foreignkey"
    )
    op.drop_column("theia_session", "repo_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "theia_session",
        sa.Column("repo_id", mysql.VARCHAR(length=128), nullable=False),
    )
    op.create_foreign_key(
        "theia_session_ibfk_3",
        "theia_session",
        "assignment_repo",
        ["repo_id"],
        ["id"],
    )
    op.alter_column(
        "theia_session",
        "assignment_id",
        existing_type=mysql.VARCHAR(length=128),
        nullable=False,
    )
    op.drop_column("theia_session", "repo_url")
    op.drop_column("theia_session", "privileged")
    op.drop_column("theia_session", "options")
    op.drop_column("theia_session", "network_locked")
    op.drop_column("theia_session", "image")
    op.drop_column("assignment", "theia_image")
    # ### end Alembic commands ###
