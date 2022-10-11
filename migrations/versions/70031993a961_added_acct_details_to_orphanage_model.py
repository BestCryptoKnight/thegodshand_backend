"""Added acct details to orphanage model

Revision ID: 70031993a961
Revises: 7e9be07a0f49
Create Date: 2022-02-12 11:17:15.884819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70031993a961'
down_revision = '7e9be07a0f49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orphanage', schema=None) as batch_op:
        batch_op.add_column(sa.Column('actId', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('acttype', sa.String(length=6), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orphanage', schema=None) as batch_op:
        batch_op.drop_column('acttype')
        batch_op.drop_column('actId')

    # ### end Alembic commands ###
