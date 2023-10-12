"""initial

Revision ID: b813e97e046c
Revises: b6ae0b65d385
Create Date: 2023-10-12 15:28:56.356845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b813e97e046c'
down_revision: Union[str, None] = 'b6ae0b65d385'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
