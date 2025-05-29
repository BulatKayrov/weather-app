import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from backend.api import router


from backend.config.conf import settings, BASE_DIR

app = FastAPI(
    title="Weather API",
    description="Simple weather API for simple application",
    version="0.1.0",
)

templates = Jinja2Templates(directory=f"{BASE_DIR}/src/frontend")

app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, host=settings.HOST, port=settings.PORT)
