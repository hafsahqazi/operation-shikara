"""empty message

Revision ID: 02f8b50cbff4
Revises: None
Create Date: 2019-01-04 22:49:56.933708

"""

# revision identifiers, used by Alembic.
revision = '02f8b50cbff4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('ID')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('organization')
    ### end Alembic commands ###
