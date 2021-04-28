"""ADD ta_for and professor_for tables

Revision ID: 3d972cfa5be9
Revises: b99d63327de0
Create Date: 2021-04-27 14:47:30.881951

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "3d972cfa5be9"
down_revision = "b99d63327de0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "professor_for_course",
        sa.Column("owner_id", sa.String(length=128), nullable=False),
        sa.Column("course_id", sa.String(length=128), nullable=False),
        sa.ForeignKeyConstraint(
            ["course_id"],
            ["course.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("owner_id", "course_id"),
    )
    op.create_table(
        "ta_for_course",
        sa.Column("owner_id", sa.String(length=128), nullable=False),
        sa.Column("course_id", sa.String(length=128), nullable=False),
        sa.ForeignKeyConstraint(
            ["course_id"],
            ["course.id"],
        ),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("owner_id", "course_id"),
    )
    op.alter_column(
        "assignment", "name", existing_type=mysql.MEDIUMTEXT(), nullable=False
    )
    op.alter_column(
        "assignment_repo",
        "github_username",
        existing_type=mysql.MEDIUMTEXT(),
        nullable=False,
    )
    op.alter_column(
        "assignment_repo",
        "repo_url",
        existing_type=mysql.MEDIUMTEXT(),
        nullable=False,
    )
    op.alter_column(
        "course",
        "course_code",
        existing_type=mysql.MEDIUMTEXT(),
        nullable=False,
    )
    op.alter_column(
        "course", "name", existing_type=mysql.MEDIUMTEXT(), nullable=False
    )
    op.alter_column(
        "course", "professor", existing_type=mysql.MEDIUMTEXT(), nullable=False
    )
    op.drop_column("user", "is_admin")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user",
        sa.Column(
            "is_admin",
            mysql.TINYINT(display_width=1),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.alter_column(
        "course", "professor", existing_type=mysql.MEDIUMTEXT(), nullable=True
    )
    op.alter_column(
        "course", "name", existing_type=mysql.MEDIUMTEXT(), nullable=True
    )
    op.alter_column(
        "course",
        "course_code",
        existing_type=mysql.MEDIUMTEXT(),
        nullable=True,
    )
    op.alter_column(
        "assignment_repo",
        "repo_url",
        existing_type=mysql.MEDIUMTEXT(),
        nullable=True,
    )
    op.alter_column(
        "assignment_repo",
        "github_username",
        existing_type=mysql.MEDIUMTEXT(),
        nullable=True,
    )
    op.alter_column(
        "assignment", "name", existing_type=mysql.MEDIUMTEXT(), nullable=True
    )
    op.drop_table("ta_for_course")
    op.drop_table("professor_for_course")
    # ### end Alembic commands ###
