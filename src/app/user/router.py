from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates


user_router = APIRouter(
    prefix="/user",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")


@user_router.get("/")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
