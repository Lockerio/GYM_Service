import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.user.router import user_router

app = FastAPI(
    title="GYM Service"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
