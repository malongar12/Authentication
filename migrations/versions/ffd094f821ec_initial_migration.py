"""Initial migration.

Revision ID: ffd094f821ec
Revises: 
Create Date: 2024-02-20 19:46:57.146416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffd094f821ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('register',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(), nullable=False),
    sa.Column('lastName', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('firstName'),
    sa.UniqueConstraint('lastName'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('register')
    # ### end Alembic commands ###
