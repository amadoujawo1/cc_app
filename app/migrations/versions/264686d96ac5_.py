"""empty message

Revision ID: 264686d96ac5
Revises: 
Create Date: 2025-01-25 20:27:25.363652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '264686d96ac5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('infants', sa.String(), nullable=True),
    sa.Column('diplomats', sa.String(), nullable=True),
    sa.Column('deportees', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('iics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('infants', sa.String(), nullable=True),
    sa.Column('diplomats', sa.String(), nullable=True),
    sa.Column('deportees', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('iics')
    op.drop_table('gia')
    # ### end Alembic commands ###
