"""empty message

Revision ID: a5ca21bde9f5
Revises: 
Create Date: 2022-05-03 22:31:39.966112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5ca21bde9f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coffee',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_coffee_id'), 'coffee', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('telegram_id', sa.BigInteger(), nullable=True),
    sa.Column('is_stuff', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('client', sa.Integer(), nullable=True),
    sa.Column('telegram_charge_id', sa.String(length=200), nullable=True),
    sa.Column('payment_charge_id', sa.String(length=200), nullable=True),
    sa.Column('coffee', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=30), nullable=True),
    sa.Column('order_number', sa.Integer(), nullable=True),
    sa.Column('order_price', sa.Integer(), nullable=True),
    sa.Column('ordered_by', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['client'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['coffee'], ['coffee.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_coffee_id'), table_name='coffee')
    op.drop_table('coffee')
    # ### end Alembic commands ###