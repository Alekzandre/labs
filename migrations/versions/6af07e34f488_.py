"""empty message

Revision ID: 6af07e34f488
Revises: 6c062d91abdc
Create Date: 2016-06-03 17:31:16.393394

"""

# revision identifiers, used by Alembic.
revision = '6af07e34f488'
down_revision = '6c062d91abdc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('registrations',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('contrat_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contrat_id'], ['contrat.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('registrations')
    ### end Alembic commands ###