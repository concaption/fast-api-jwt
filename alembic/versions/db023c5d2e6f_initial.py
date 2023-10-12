"""initial

Revision ID: db023c5d2e6f
Revises: c79f36aef215
Create Date: 2023-10-12 15:44:47.933525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db023c5d2e6f'
down_revision: Union[str, None] = 'c79f36aef215'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
