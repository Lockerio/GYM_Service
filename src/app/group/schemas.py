from pydantic import BaseModel, PositiveInt


class GroupCreateOrUpdate(BaseModel):
    title: str
    customer_amount: PositiveInt
    