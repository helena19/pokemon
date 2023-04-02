from pydantic import BaseModel

class StatDetails(BaseModel):
    name: str


class Stat(BaseModel):
    details: StatDetails
    base_stat: int


class PokemonCard(BaseModel):
    name: str
    height: int
    weight: int
    stats: list[Stat]

    class Config:
        orm_mode = True


class BattleResult(BaseModel):
    pokemon_1: PokemonCard
    pokemon_2: PokemonCard
    winner: PokemonCard
    message: str
