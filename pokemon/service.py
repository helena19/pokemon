from pokemon import models
from pokemon import schema
from pokemon import battle
from pokemon.pokeapi import client

def get_pokemon_card(pokemon_name: str) -> schema.PokemonCard:
    pokemon_client = client.PokemonClient()
    pokemon = pokemon_client.get_pokemon_by_name(name=pokemon_name)
    pokemon_card = schema.PokemonCard.from_orm(pokemon)
    return pokemon_card    


def perform_pokemon_battle(
    pokemon_name_1: str, 
    pokemon_name_2: str,
) -> schema.BattleResult:
    pokemon_card_1 = get_pokemon_card(pokemon_name_1)
    pokemon_card_2 = get_pokemon_card(pokemon_name_2)

    pokemon_1 = models.Pokemon.from_pokemon_card(pokemon_card_1)
    pokemon_2 = models.Pokemon.from_pokemon_card(pokemon_card_2)

    winner = battle.fight(
        pokemon_1=pokemon_1,
        pokemon_2=pokemon_2,
    )

    battle_result = schema.BattleResult(
        pokemon_1=models.Pokemon.to_pokemon_card(pokemon=pokemon_1),
        pokemon_2=models.Pokemon.to_pokemon_card(pokemon=pokemon_2),
        winner=models.Pokemon.to_pokemon_card(pokemon=winner),
        message=f'Battle is over, winner is {winner.name}'
    )

    return battle_result
