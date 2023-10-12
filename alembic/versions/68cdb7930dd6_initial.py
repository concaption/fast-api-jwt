"""initial

Revision ID: 68cdb7930dd6
Revises: 4614d9bd4d41
Create Date: 2023-10-12 15:16:03.487752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68cdb7930dd6'
down_revision: Union[str, None] = '4614d9bd4d41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
