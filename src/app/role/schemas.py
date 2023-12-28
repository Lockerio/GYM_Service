from pydantic import BaseModel


class RoleCreateOrUpdate(BaseModel):
    title: str
