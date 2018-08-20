"""empty message

Revision ID: 489d7a5acea7
Revises: 
Create Date: 2018-08-20 23:29:06.134678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '489d7a5acea7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('good',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('good_pic_url', sa.String(length=20), nullable=False),
    sa.Column('good_price', sa.Integer(), nullable=False),
    sa.Column('good_name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=20), nullable=False),
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('good_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['good_id'], ['good.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('good')
    # ### end Alembic commands ###