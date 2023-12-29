from fastapi import APIRouter, Request, Form, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates

from app.db.dal.group_dao import GroupDAO
from app.db.dal.role_dao import RoleDAO
from app.db.session import get_session
from app.role.schemas import RoleCreateOrUpdate

group_router = APIRouter(
    prefix="/group"
)

templates = Jinja2Templates(directory="app/group/templates")


@group_router.get("/create")
async def create(request: Request):
    return templates.TemplateResponse("group_create.html", {"request": request})


@group_router.post("/group_created")
async def created(
        request: Request,
        title: str = Form(...),
        customer_amount: int = Form(...),
        session: AsyncSession = Depends(get_session)
):
    body = RoleCreateOrUpdate(
        title=title,
        customer_amount=customer_amount
    )

    async with session.begin():
        group_dao = GroupDAO(session)

        group = await group_dao.create_group(
            title=body.title
        )

    return templates.TemplateResponse("group_created.html", {"request": request, "group": group})
