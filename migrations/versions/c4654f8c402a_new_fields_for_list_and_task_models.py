"""new fields for List and Task models

Revision ID: c4654f8c402a
Revises: 30b24326fbfc
Create Date: 2018-01-09 16:04:52.349023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4654f8c402a'
down_revision = '30b24326fbfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('list', sa.Column('pin_hash', sa.String(length=128), nullable=True))
    op.add_column('task', sa.Column('do_by', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('priority', sa.String(length=6), nullable=True))
    op.create_index(op.f('ix_task_do_by'), 'task', ['do_by'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_do_by'), table_name='task')
    op.drop_column('task', 'priority')
    op.drop_column('task', 'do_by')
    op.drop_column('list', 'pin_hash')
    # ### end Alembic commands ###
