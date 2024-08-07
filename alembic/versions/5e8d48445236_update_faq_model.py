"""update faq model

Revision ID: 5e8d48445236
Revises: d97cd1f6afa7
Create Date: 2024-08-07 13:34:14.694816

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e8d48445236'
down_revision: Union[str, None] = 'd97cd1f6afa7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('faqs', sa.Column('category', sa.String(), nullable=True))
    op.alter_column('faqs', 'question',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('faqs', 'answer',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('faqs', 'answer',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('faqs', 'question',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('faqs', 'category')
    # ### end Alembic commands ###