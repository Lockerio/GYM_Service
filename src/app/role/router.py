from fastapi import APIRouter, Request, Form, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates

from app.db.dal.role_dao import RoleDAO
from app.db.session import get_session
from app.role.schemas import RoleCreateOrUpdate

role_router = APIRouter(
    prefix="/role"
)

templates = Jinja2Templates(directory="app/role/templates")


@role_router.get("/create")
async def create(request: Request):
    return templates.TemplateResponse("role_create.html", {"request": request})


@role_router.post("/role_created")
async def created(
        request: Request,
        title: str = Form(...),
        session: AsyncSession = Depends(get_session)
):
    body = RoleCreateOrUpdate(
        title=title,
    )

    async with session.begin():
        role_dao = RoleDAO(session)

        role = await role_dao.create_role(
            title=body.title
        )

    return templates.TemplateResponse("role_created.html", {"request": request, "role": role})
