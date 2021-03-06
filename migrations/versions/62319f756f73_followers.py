"""followers

Revision ID: 62319f756f73
Revises: 31140c807be3
Create Date: 2019-06-27 14:19:27.419627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62319f756f73'
down_revision = '31140c807be3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
