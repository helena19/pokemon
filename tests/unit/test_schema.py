import pytest

from pokemon.pokeapi import schema
from tests.data import pokemon_data

class TestPokemon:
    @pytest.mark.parametrize(
        'pokemon_name, pokemon_data',
        [
            ('pikachu', pokemon_data.pikachu_data),
            ('eevee', pokemon_data.eevee_data),
        ]
    )
    def test_ok(self, pokemon_name, pokemon_data):
        # arrange & act
        pokemon = schema.Pokemon.parse_obj(pokemon_data)

        # assert
        assert pokemon.id == pokemon_data['id']
        assert pokemon.name == pokemon_name
        assert pokemon.order == pokemon_data['order']
        assert pokemon.base_experience == pokemon_data['base_experience']
        assert pokemon.height == pokemon_data['height']
        assert pokemon.weight == pokemon_data['weight']
        assert len(pokemon.stats) == 6