"""add_user_logging_table

Revision ID: 6a4383fc4a4f
Revises: ae4417d921f2
Create Date: 2020-07-21 15:50:35.521572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a4383fc4a4f'
down_revision = 'ae4417d921f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_loggings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('log_datetime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_loggings_user_id'), 'user_loggings', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_loggings_user_id'), table_name='user_loggings')
    op.drop_table('user_loggings')
    # ### end Alembic commands ###
