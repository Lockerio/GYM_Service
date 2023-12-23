import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

app = FastAPI(
    title="GYM Service"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
