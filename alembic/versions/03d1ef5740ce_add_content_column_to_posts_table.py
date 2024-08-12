"""add content column to posts table

Revision ID: 03d1ef5740ce
Revises: 2b39d1264924
Create Date: 2024-08-12 14:49:43.984146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03d1ef5740ce'
down_revision: Union[str, None] = '2b39d1264924'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
