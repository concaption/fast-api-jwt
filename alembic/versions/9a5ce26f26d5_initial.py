"""initial

Revision ID: 9a5ce26f26d5
Revises: 215bc0eb0245
Create Date: 2023-10-12 15:41:35.728953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a5ce26f26d5'
down_revision: Union[str, None] = '215bc0eb0245'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
