from fastapi import APIRouter

from pokemon import schema
from pokemon import service

router = APIRouter()

@router.get("/")
async def root() -> dict:
    return {"message": "Welcome to the battle ϞϞ〈๑⚈ ․̫⚈๑〉"}


@router.get("/pokemon_card/{name}")
async def get_pokemon_card(name: str) -> schema.PokemonCard:
    pokemon_card = service.get_pokemon_card(name)
    return pokemon_card


@router.get("/pokemon_battle/{first_pokemon}/vs/{second_pokemon}")
async def get_pokemon_battle_result(
    first_pokemon: str, second_pokemon: str
) -> schema.BattleResult:
    battle_result = service.perform_pokemon_battle(
        pokemon_name_1=first_pokemon,
        pokemon_name_2=second_pokemon,
    )
    return battle_result
    