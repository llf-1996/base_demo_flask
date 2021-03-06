"""add mobile

Revision ID: f58dcf064bb1
Revises: 31a9a4ec5557
Create Date: 2019-03-03 21:35:54.250943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f58dcf064bb1'
down_revision = '31a9a4ec5557'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_authors', sa.Column('mobile', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_authors', 'mobile')
    # ### end Alembic commands ###
