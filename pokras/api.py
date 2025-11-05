from fastapi import APIRouter

router = APIRouter()

@router.get("/game")
async def get_game_state():
    return {"message": "Game state"}
