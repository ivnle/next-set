"""empty message

Revision ID: 38e6cecd3849
Revises: e0a00045f6c7
Create Date: 2019-07-21 09:22:24.303125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38e6cecd3849'
down_revision = 'e0a00045f6c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('set_anon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('exercise', sa.String(length=128), nullable=True),
    sa.Column('pounds', sa.Integer(), nullable=True),
    sa.Column('reps', sa.Integer(), nullable=True),
    sa.Column('rpe', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=140), nullable=True),
    sa.Column('bodyweight', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_set_anon_timestamp'), 'set_anon', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_set_anon_timestamp'), table_name='set_anon')
    op.drop_table('set_anon')
    # ### end Alembic commands ###