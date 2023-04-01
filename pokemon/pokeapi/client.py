import requests
import json

class PokemonClient():
    base_url = 'https://pokeapi.co/api'
    api_version = 'v2'

    @classmethod
    def get_pokemon_by_name(self, name: str) -> json:
        url = f'{self.base_url}/{self.api_version}/pokemon/{name}' 
        response = requests.get(url)

        

        return response.json()