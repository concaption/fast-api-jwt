"""initial

Revision ID: b6ae0b65d385
Revises: fb7c686b6d0d
Create Date: 2023-10-12 15:27:10.846316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6ae0b65d385'
down_revision: Union[str, None] = 'fb7c686b6d0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
