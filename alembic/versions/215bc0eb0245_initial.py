"""initial

Revision ID: 215bc0eb0245
Revises: b813e97e046c
Create Date: 2023-10-12 15:36:18.883400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '215bc0eb0245'
down_revision: Union[str, None] = 'b813e97e046c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
