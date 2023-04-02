import pytest
import requests_mock

from pokemon.pokeapi import client
from tests.data import pokemon_data

class TestClient:
    @pytest.mark.parametrize(
        'pokemon_name, pokemon_data',
        [
            ('pikachu', pokemon_data.pikachu_data),
            ('eevee', pokemon_data.eevee_data),
        ]
    )
    def test_get_pokemon_by_name(self, pokemon_name, pokemon_data) -> None:
        # arrange
        pokemon_client = client.PokemonClient()

        # act
        with requests_mock.mock() as m:
            m.get(
                f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}',
                json=pokemon_data,
            )
            pokemon_card = pokemon_client.get_pokemon_by_name(pokemon_name)
            
        # assert
        assert pokemon_card
        assert pokemon_card.id == pokemon_data['id']
        assert pokemon_card.name == pokemon_name
        assert pokemon_card.order == pokemon_data['order']
        assert pokemon_card.base_experience == pokemon_data['base_experience']
        assert pokemon_card.height == pokemon_data['height']
        assert pokemon_card.weight == pokemon_data['weight']
        assert len(pokemon_card.stats) == 6
