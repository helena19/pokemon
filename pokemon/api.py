from fastapi import APIRouter, HTTPException

from pokemon import schema
from pokemon import service
from pokemon.pokeapi import exceptions as pokeapi_exc

router = APIRouter()

@router.get("/")
async def root() -> dict:
    return {"message": "Welcome to the battle ϞϞ〈๑⚈ ․̫⚈๑〉"}


@router.get("/pokemon_card/{name}")
async def get_pokemon_card(name: str) -> schema.PokemonCard:
    try:
        pokemon_card = service.get_pokemon_card(name)
    except pokeapi_exc.ServerError:
        raise HTTPException(
            status_code=503, 
            detail="Provider's service is unavailable",
        )
    except (pokeapi_exc.ClientError, pokeapi_exc.ValidationError):
        raise HTTPException(
            status_code=500,
            detail="Failed to execute remote request",
        )

    return pokemon_card
    

@router.get("/pokemon_battle/{first_pokemon}/vs/{second_pokemon}")
async def get_pokemon_battle_result(
    first_pokemon: str, second_pokemon: str
) -> schema.BattleResult:
    try:
        battle_result = service.perform_pokemon_battle(
            pokemon_name_1=first_pokemon,
            pokemon_name_2=second_pokemon,
        )
    except pokeapi_exc.ServerError:
        raise HTTPException(
            status_code=503, 
            detail="Provider's service is unavailable",
        )
    except (pokeapi_exc.ClientError, pokeapi_exc.ValidationError):
        raise HTTPException(
            status_code=500,
            detail="Failed to execute remote request",
        )
    
    return battle_result
    