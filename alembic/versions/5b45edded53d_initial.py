"""initial

Revision ID: 5b45edded53d
Revises: db023c5d2e6f
Create Date: 2023-10-12 15:45:06.928479

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b45edded53d'
down_revision: Union[str, None] = 'db023c5d2e6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
