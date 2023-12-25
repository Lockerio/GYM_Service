from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates


user_router = APIRouter(
    prefix="/user",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="app/user/templates")


@user_router.get("/")
def get_base_page(request: Request):
    user = {
        "first_name": "gui",
        "last_name": "petrov"
    }
    return templates.TemplateResponse("user_profile.html", {"request": request, "user": user})
