from fastapi import APIRouter
from starlette.templating import Jinja2Templates


user_router = APIRouter(
    prefix="/role"
)

templates = Jinja2Templates(directory="app/role/templates")
