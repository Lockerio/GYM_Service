from uuid import UUID

from fastapi import APIRouter, Request, Depends, Form, Path
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.routing import NoMatchFound
from starlette.templating import Jinja2Templates

from app.db.dal.user_dao import UserDAO
from app.db.session import get_session
from app.hashing import Hasher
from app.user.schemas import UserCreate

user_router = APIRouter(
    prefix="/user"
)

templates = Jinja2Templates(directory="app/user/templates")


@user_router.get("/{user_uuid}")
async def user_profile(request: Request, user_uuid: UUID = Path(...), session: AsyncSession = Depends(get_session)):
    async with session.begin():
        user_dao = UserDAO(session)

        user = await user_dao.get_user_by_id(
            user_id=user_uuid
        )

    if user:
        return templates.TemplateResponse("user_profile.html", {"request": request, "user": user})
    return templates.TemplateResponse("user_not_found.html", {"request": request})


@user_router.get("/create")
async def create(request: Request):
    return templates.TemplateResponse("user_create.html", {"request": request})


@user_router.post("/created")
async def created(
        request: Request,
        first_name: str = Form(...),
        last_name: str = Form(...),
        father_name: str = Form(...),
        password: str = Form(...),
        email: str = Form(...),
        session: AsyncSession = Depends(get_session)
):
    body = UserCreate(
        first_name=first_name,
        last_name=last_name,
        father_name=father_name,
        password=password,
        email=email,
    )

    async with session.begin():
        user_dao = UserDAO(session)

        user = await user_dao.create_user(
            first_name=body.first_name,
            last_name=body.last_name,
            father_name=body.father_name,
            hashed_password=Hasher.get_password_hash(body.password),
            email=body.email,
        )

    return templates.TemplateResponse("user_created.html", {"request": request, "user": user})
