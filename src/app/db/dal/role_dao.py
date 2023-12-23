from typing import Union

from sqlalchemy import update, and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Role


class RoleDAO:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_role(self, title: str) -> Role:
        new_role = Role(title=title)
        self.db_session.add(new_role)
        await self.db_session.flush()
        return new_role

    async def get_role_by_id(self, role_id: int) -> Union[Role, None]:
        query = select(Role).where(Role.role_id == role_id)
        res = await self.db_session.execute(query)
        role_row = res.fetchone()
        if role_row is not None:
            return role_row[0]

    async def update_role(self, role_id: int, title: str) -> Union[int, None]:
        query = (
            update(Role)
            .where(Role.role_id == role_id)
            .values(title=title)
            .returning(Role.role_id)
        )
        res = await self.db_session.execute(query)
        updated_role_id_row = res.fetchone()
        if updated_role_id_row is not None:
            return updated_role_id_row[0]
