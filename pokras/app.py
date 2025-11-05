import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pokras.api import router

app = FastAPI()

app.mount("/static", StaticFiles(directory="pokras/static"), name="static")
app.include_router(router)


@app.get("/")
async def read_root():
    return FileResponse('pokras/static/index.html')
