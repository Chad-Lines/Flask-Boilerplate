"""customer table

Revision ID: 02a5122a14ae
Revises: 8149b740866b
Create Date: 2019-10-31 16:32:31.483960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02a5122a14ae'
down_revision = '8149b740866b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('middleinit', sa.String(length=1), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('address1', sa.String(length=64), nullable=True),
    sa.Column('address2', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=64), nullable=True),
    sa.Column('postal', sa.Integer(), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_address1'), 'customer', ['address1'], unique=False)
    op.create_index(op.f('ix_customer_address2'), 'customer', ['address2'], unique=False)
    op.create_index(op.f('ix_customer_city'), 'customer', ['city'], unique=False)
    op.create_index(op.f('ix_customer_created'), 'customer', ['created'], unique=False)
    op.create_index(op.f('ix_customer_email'), 'customer', ['email'], unique=True)
    op.create_index(op.f('ix_customer_firstname'), 'customer', ['firstname'], unique=False)
    op.create_index(op.f('ix_customer_lastname'), 'customer', ['lastname'], unique=False)
    op.create_index(op.f('ix_customer_middleinit'), 'customer', ['middleinit'], unique=False)
    op.create_index(op.f('ix_customer_phone'), 'customer', ['phone'], unique=True)
    op.create_index(op.f('ix_customer_postal'), 'customer', ['postal'], unique=False)
    op.create_index(op.f('ix_customer_state'), 'customer', ['state'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_customer_state'), table_name='customer')
    op.drop_index(op.f('ix_customer_postal'), table_name='customer')
    op.drop_index(op.f('ix_customer_phone'), table_name='customer')
    op.drop_index(op.f('ix_customer_middleinit'), table_name='customer')
    op.drop_index(op.f('ix_customer_lastname'), table_name='customer')
    op.drop_index(op.f('ix_customer_firstname'), table_name='customer')
    op.drop_index(op.f('ix_customer_email'), table_name='customer')
    op.drop_index(op.f('ix_customer_created'), table_name='customer')
    op.drop_index(op.f('ix_customer_city'), table_name='customer')
    op.drop_index(op.f('ix_customer_address2'), table_name='customer')
    op.drop_index(op.f('ix_customer_address1'), table_name='customer')
    op.drop_table('customer')
    # ### end Alembic commands ###