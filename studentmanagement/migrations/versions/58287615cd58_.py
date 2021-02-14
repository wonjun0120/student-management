"""empty message

Revision ID: 58287615cd58
Revises: 
Create Date: 2021-02-14 21:21:30.467874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58287615cd58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('major',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('professor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=20), nullable=True),
    sa.Column('birth', sa.Date(), nullable=True),
    sa.Column('phone', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('major', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['major'], ['major.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=20), nullable=True),
    sa.Column('birth', sa.Date(), nullable=True),
    sa.Column('phone', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('major', sa.Integer(), nullable=True),
    sa.Column('admission_date', sa.Date(), nullable=True),
    sa.Column('semester', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['major'], ['major.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('lecture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('opened_grade', sa.Integer(), nullable=True),
    sa.Column('grades', sa.Integer(), nullable=True),
    sa.Column('major', sa.Integer(), nullable=True),
    sa.Column('professor', sa.Integer(), nullable=True),
    sa.Column('place', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['major'], ['major.id'], ),
    sa.ForeignKeyConstraint(['professor'], ['professor.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('lecture_student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student', sa.Integer(), nullable=True),
    sa.Column('lecture', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lecture'], ['lecture.id'], ),
    sa.ForeignKeyConstraint(['student'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('lecture_time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lecture', sa.Integer(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['lecture'], ['lecture.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_general_ci'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lecture_time')
    op.drop_table('lecture_student')
    op.drop_table('lecture')
    op.drop_table('student')
    op.drop_table('professor')
    op.drop_table('major')
    # ### end Alembic commands ###