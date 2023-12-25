from fastapi import APIRouter, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates

from app.db.dal.user_dao import UserDAO
from app.db.session import get_db
from app.hashing import Hasher
from app.user.schemas import UserCreate

user_router = APIRouter(
    prefix="/user"
)

templates = Jinja2Templates(directory="app/user/templates")


@user_router.get("/")
async def user_profile(request: Request):
    user = {
        "first_name": "gui",
        "last_name": "petrov"
    }
    return templates.TemplateResponse("user_profile.html", {"request": request, "user": user})


@user_router.get("/create")
async def create(request: Request):
    return templates.TemplateResponse("user_create.html", {"request": request})


@user_router.get("/created")
async def created(request: Request, body: UserCreate, session: AsyncSession = Depends(get_db)):
    async with session.begin():
        user_dao = UserDAO(session)

        user = await user_dao.create_user(
            first_name=body.first_name,
            last_name=body.last_name,
            father_name=body.father_name,
            hashed_password=Hasher.get_password_hash(body.password),
        )

    return templates.TemplateResponse("user_created.html", {"request": request, "user": user})
