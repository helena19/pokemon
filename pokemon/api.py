from fastapi import APIRouter

from pokeapi import client
from pokeapi import schema

router = APIRouter()

@router.get("/")
async def root() -> dict:
    return {"message": "Welcome to the battle ϞϞ〈๑⚈ ․̫⚈๑〉"}


@router.get("/pokemon_card/{name}")
async def get_pokemon_card(name: str) -> schema.Pokemon:
    pokemon_client = client.PokemonClient()
    pokemon_card = pokemon_client.get_pokemon_by_name(name=name)
    return pokemon_card
