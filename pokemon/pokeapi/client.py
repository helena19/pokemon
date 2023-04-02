import requests

from pydantic import ValidationError
from pokemon.pokeapi import exceptions as exc
from pokemon.pokeapi import schema

class PokemonClient():
    base_url = 'https://pokeapi.co/api'
    api_version = 'v2'

    @classmethod
    def get_pokemon_by_name(self, name: str) -> schema.Pokemon:
        url = f'{self.base_url}/{self.api_version}/pokemon/{name}'
        response = requests.get(url)

        if 400 <= response.status_code <= 499:
            raise exc.ClientError(response.reason)
        elif 500 <= response.status_code <= 599:
            raise exc.ServerError(response.reason)

        try:
            result = response.json()
            pokemon = schema.Pokemon.parse_obj(result)
        except ValidationError:
            raise exc.ValidationError

        return pokemon
