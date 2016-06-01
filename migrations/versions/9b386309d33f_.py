"""empty message

Revision ID: 9b386309d33f
Revises: a72cd3955497
Create Date: 2016-06-01 16:47:04.717673

"""

# revision identifiers, used by Alembic.
revision = '9b386309d33f'
down_revision = 'a72cd3955497'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contrat', sa.Column('used_slot', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contrat', 'used_slot')
    ### end Alembic commands ###
