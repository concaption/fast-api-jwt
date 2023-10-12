"""initial

Revision ID: d28933248e8e
Revises: 9a5ce26f26d5
Create Date: 2023-10-12 15:42:55.762983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd28933248e8e'
down_revision: Union[str, None] = '9a5ce26f26d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
