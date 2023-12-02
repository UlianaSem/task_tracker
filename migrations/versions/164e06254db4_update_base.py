"""Update Base

Revision ID: 164e06254db4
Revises: a0914bc9e808
Create Date: 2023-12-02 12:56:33.886772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '164e06254db4'
down_revision: Union[str, None] = 'a0914bc9e808'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'performer',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('tasks_performer_fkey', 'tasks', type_='foreignkey')
    op.create_foreign_key(None, 'tasks', 'employees', ['performer'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.create_foreign_key('tasks_performer_fkey', 'tasks', 'employees', ['performer'], ['id'], ondelete='CASCADE')
    op.alter_column('tasks', 'performer',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
