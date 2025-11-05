from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pokras.db.base import Base
from pokras.db.engine import engine

# Import all the models so that they are registered with SQLAlchemy's metadata
from pokras.modules.game.models.game import Game
from pokras.modules.country.models.country import Country
from pokras.modules.roll.models.tile import Tile
from pokras.modules.roll.models.last_roll import LastRoll

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Determine the absolute path to the project root.
# This is necessary for Vercel's serverless environment where the working directory is different.
# The app.py file is inside the 'pokras' directory, so we need to go up one level.
root_dir = Path(__file__).parent.parent
static_files_path = root_dir / "static"

app.mount("/static", StaticFiles(directory=static_files_path), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    index_html_path = static_files_path / "index.html"
    with open(index_html_path, "r") as f:
        return f.read()
