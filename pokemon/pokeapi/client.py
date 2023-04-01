import requests

from pokemon.pokeapi import schema

class PokemonClient():
    base_url = 'https://pokeapi.co/api'
    api_version = 'v2'

    @classmethod
    def get_pokemon_by_name(self, name: str) -> schema.Pokemon:
        url = f'{self.base_url}/{self.api_version}/pokemon/{name}' 
        response = requests.get(url).json()
        pokemon = schema.Pokemon.parse_obj(response)
        return pokemon
