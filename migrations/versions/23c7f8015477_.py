"""empty message

Revision ID: 23c7f8015477
Revises: a5cffa318ac2
Create Date: 2023-12-14 10:19:47.870587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23c7f8015477'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.Column('hair_color', sa.String(), nullable=False),
    sa.Column('skin_color', sa.String(), nullable=False),
    sa.Column('eye_color', sa.String(), nullable=False),
    sa.Column('birth_year', sa.String(), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('created', sa.String(), nullable=False),
    sa.Column('edited', sa.String(), nullable=False),
    sa.Column('homeworld', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('img', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('img'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.String(), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.Column('gravity', sa.String(), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(), nullable=False),
    sa.Column('terrain', sa.String(), nullable=False),
    sa.Column('surface_water', sa.Boolean(), nullable=False),
    sa.Column('created', sa.String(), nullable=False),
    sa.Column('edited', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('starship_class', sa.String(), nullable=False),
    sa.Column('cost_in_credits', sa.Integer(), nullable=False),
    sa.Column('length', sa.Integer(), nullable=False),
    sa.Column('crew', sa.Integer(), nullable=False),
    sa.Column('passengers', sa.Integer(), nullable=False),
    sa.Column('max_atmosphere_speed', sa.Integer(), nullable=False),
    sa.Column('hyperdrive_rating', sa.String(), nullable=False),
    sa.Column('MGLT', sa.Integer(), nullable=False),
    sa.Column('cargo_capacity', sa.Integer(), nullable=False),
    sa.Column('consumables', sa.String(), nullable=False),
    sa.Column('created', sa.String(), nullable=False),
    sa.Column('edited', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('starships')
    op.drop_table('planets')
    op.drop_table('items')
    op.drop_table('characters')
    # ### end Alembic commands ###
