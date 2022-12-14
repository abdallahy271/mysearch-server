"""empty message

Revision ID: 626530312ac7
Revises: 2b8fc0a7ac25
Create Date: 2022-10-01 21:32:21.857298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '626530312ac7'
down_revision = '2b8fc0a7ac25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('files', sa.Column('title', sa.String(length=200), nullable=True))
    op.drop_column('files', 'titles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('files', sa.Column('titles', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    op.drop_column('files', 'title')
    # ### end Alembic commands ###
