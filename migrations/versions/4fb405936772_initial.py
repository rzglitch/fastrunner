"""Initial

Revision ID: 4fb405936772
Revises: 
Create Date: 2024-05-30 19:48:57.735384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fb405936772'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.BigInteger().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('display_name', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=191), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('board', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_board_display_name'), ['display_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_board_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_board_uuid'), ['uuid'], unique=True)

    op.create_table('entry',
    sa.Column('id', sa.BigInteger().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('parent', sa.BigInteger().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('entry_metadata', sa.Text(), nullable=False),
    sa.Column('user_id', sa.BigInteger().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.Column('hits', sa.BigInteger().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.Column('likes', sa.BigInteger().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.Column('created_at', sa.BigInteger().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.Column('modified_at', sa.BigInteger().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('entry', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_entry_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_deleted'), ['deleted'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_hits'), ['hits'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_likes'), ['likes'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_modified_at'), ['modified_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_parent'), ['parent'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_title'), ['title'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_user_id'), ['user_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_entry_uuid'), ['uuid'], unique=True)

    op.create_table('user',
    sa.Column('id', sa.BigInteger().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=191), nullable=False),
    sa.Column('display_name', sa.String(length=64), nullable=False),
    sa.Column('group', sa.BigInteger().with_variant(sa.Integer(), 'sqlite'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_display_name'), ['display_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_group'), ['group'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_uuid'), ['uuid'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_uuid'))
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_group'))
        batch_op.drop_index(batch_op.f('ix_user_display_name'))

    op.drop_table('user')
    with op.batch_alter_table('entry', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_entry_uuid'))
        batch_op.drop_index(batch_op.f('ix_entry_user_id'))
        batch_op.drop_index(batch_op.f('ix_entry_title'))
        batch_op.drop_index(batch_op.f('ix_entry_parent'))
        batch_op.drop_index(batch_op.f('ix_entry_modified_at'))
        batch_op.drop_index(batch_op.f('ix_entry_likes'))
        batch_op.drop_index(batch_op.f('ix_entry_hits'))
        batch_op.drop_index(batch_op.f('ix_entry_deleted'))
        batch_op.drop_index(batch_op.f('ix_entry_created_at'))

    op.drop_table('entry')
    with op.batch_alter_table('board', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_board_uuid'))
        batch_op.drop_index(batch_op.f('ix_board_name'))
        batch_op.drop_index(batch_op.f('ix_board_display_name'))

    op.drop_table('board')
    # ### end Alembic commands ###
