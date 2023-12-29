from typing import Union

from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import GroupType


class GroupDAO:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_group(self, title: str) -> GroupType:
        new_group = GroupType(title=title)
        self.db_session.add(new_group)
        await self.db_session.flush()
        return new_group

    async def get_group_by_id(self, group_id: int) -> Union[GroupType, None]:
        query = select(GroupType).where(GroupType.groupType_id == group_id)
        res = await self.db_session.execute(query)
        group_row = res.fetchone()
        if group_row is not None:
            return group_row[0]

    async def update_group(self, group_id: int, title: str, customer_amount: int) -> Union[int, None]:
        query = (
            update(GroupType)
            .where(GroupType.groupType_id == group_id)
            .values(title=title, customer_amount=customer_amount)
            .returning(GroupType.groupType_id)
        )
        res = await self.db_session.execute(query)
        updated_group_id_row = res.fetchone()
        if updated_group_id_row is not None:
            return updated_group_id_row[0]
