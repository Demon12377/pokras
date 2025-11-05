from fastapi import APIRouter, HTTPException
# from sqlalchemy.orm import joinedload
# from pokras.db.engine import Session
# from pokras.modules.game.models.game import Game, GameMap
# from pokras.modules.country.models.country import Country
# from pokras.modules.roll.models.tile import Tile
# from pokras.schemas import CountryCreate

router = APIRouter()

@router.get("/game")
async def get_game_state():
    return {
        "territories": {},
        "countries": [],
    }
    # with Session() as session:
    #     game = session.query(Game).first()
    #     if not game:
    #         game = Game(channel=0, is_active=True, map=GameMap.eu_classic, roll_values="1,2,3,4,5,6")
    #         session.add(game)
    #         session.commit()

    #     countries = session.query(Country).options(joinedload(Country.tiles)).filter(Country.game_id == game.id).all()

    #     territories = {}
    #     for country in countries:
    #         for tile in country.tiles:
    #             territories[tile.code] = country.color

    #     return {
    #         "territories": territories,
    #         "countries": [
    #             {
    #                 "name": country.name,
    #                 "color": country.color,
    #                 "industrial": country.industrial,
    #                 "military": country.military,
    #                 "economic": country.economic,
    #             }
    #             for country in countries
    #         ],
    #     }

# @router.post("/countries")
# async def create_country(country_data: CountryCreate):
#     with Session() as session:
#         game = session.query(Game).first()
#         if not game:
#             raise HTTPException(status_code=404, detail="Game not found")

#         # Check if the territory is already claimed
#         tile = session.query(Tile).filter(Tile.game_id == game.id, Tile.code == country_data.territory).first()
#         if tile and tile.owner_id:
#             raise HTTPException(status_code=400, detail="Territory already claimed")

#         # Create the new country
#         new_country = Country(
#             name=country_data.name,
#             color=country_data.color,
#             creator_id=0,  # We'll need to handle user authentication later
#             game_id=game.id,
#             industrial=1,
#             military=1,
#             economic=1
#         )
#         session.add(new_country)
#         session.commit()

#         # Claim the starting territory
#         if not tile:
#             tile = Tile(code=country_data.territory, game_id=game.id)
#             session.add(tile)
#         tile.owner_id = new_country.id
#         session.commit()

#         return {"message": "Country created successfully"}
