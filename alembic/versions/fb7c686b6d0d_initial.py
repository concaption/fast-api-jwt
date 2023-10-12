"""initial

Revision ID: fb7c686b6d0d
Revises: 68cdb7930dd6
Create Date: 2023-10-12 15:18:51.981399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb7c686b6d0d'
down_revision: Union[str, None] = '68cdb7930dd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
