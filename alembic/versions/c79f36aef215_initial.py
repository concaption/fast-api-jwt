"""initial

Revision ID: c79f36aef215
Revises: d28933248e8e
Create Date: 2023-10-12 15:44:42.192228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c79f36aef215'
down_revision: Union[str, None] = 'd28933248e8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
