import pytest
import requests_mock

from pokemon.pokeapi import client
from pokemon.pokeapi import exceptions as exc
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
    

    def test_server_error_raises(self) -> None:
        # arrange
        pokemon_client = client.PokemonClient()

        # act & assert
        with requests_mock.mock() as m:
            m.get(
                f'https://pokeapi.co/api/v2/pokemon/pikachu',
                status_code=500,
            )
        
            with pytest.raises(exc.ServerError):
                pokemon_client.get_pokemon_by_name('pikachu')


    def test_client_error_raises(self) -> None:
        # arrange
        pokemon_client = client.PokemonClient()

        # act & assert
        with requests_mock.mock() as m:
            m.get(
                f'https://pokeapi.co/api/v2/pokemon/pikachu',
                status_code=400,
            )
        
            with pytest.raises(exc.ClientError):
                pokemon_client.get_pokemon_by_name('pikachu')


    def test_validation_error_raises(self) -> None:
        # arrange
        pokemon_client = client.PokemonClient()

        # act & assert
        with requests_mock.mock() as m:
            m.get(
                f'https://pokeapi.co/api/v2/pokemon/pikachu',
                status_code=200,
                json={
                    'invalid': 'data',
                }
            )
        
            with pytest.raises(exc.ValidationError):
                pokemon_client.get_pokemon_by_name('pikachu')


    def test_resource_not_found(self) -> None:
        # arrange
        pokemon_client = client.PokemonClient()

        # act & assert
        with requests_mock.mock() as m:
            m.get(
                f'https://pokeapi.co/api/v2/pokemon/unknown',
                status_code=404,
            )
        
            with pytest.raises(exc.ResourceNotFound):
                pokemon_client.get_pokemon_by_name('unknown')