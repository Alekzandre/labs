"""add role

Revision ID: 322a3374b317
Revises: 1072b41deb37
Create Date: 2016-05-19 22:40:46.787700

"""

# revision identifiers, used by Alembic.
revision = '322a3374b317'
down_revision = '1072b41deb37'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_role_name'), 'role', ['name'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_role_name'), table_name='role')
    op.drop_table('role')
    ### end Alembic commands ###
