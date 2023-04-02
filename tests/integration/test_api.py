import pytest
import requests_mock
from fastapi.testclient import TestClient

from pokemon.app import create_app
from tests.data import pokemon_data

app = create_app()
client = TestClient(app)

class TestApiRoot:
    def test_ok(self) -> None:
        # arrange & act
        response = client.get("/")

        # assert
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to the battle ϞϞ〈๑⚈ ․̫⚈๑〉"}
        
    
class TestApiPokemonCard:
    @pytest.mark.parametrize(
        'pokemon_name, pokemon_data, pokemon_card_data',
        [
            ('pikachu', pokemon_data.pikachu_data, pokemon_data.pikachu_card_data),
            ('eevee', pokemon_data.eevee_data, pokemon_data.eevee_card_data),
        ]
    )
    def test_ok(self, pokemon_name, pokemon_data, pokemon_card_data) -> None:
        # arrange & act
        with requests_mock.mock() as m:
            m.get(
                f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}',
                json=pokemon_data,
            )
            response = client.get(f"/pokemon_card/{pokemon_name}")

        # assert
        assert response.status_code == 200
        assert response.json() == pokemon_card_data


class TestApiPokemonBattle:
    @pytest.mark.parametrize(
        'pokemon_name_1, pokemon_name_2, battle_result',
        [
            ('eevee', 'pikachu', pokemon_data.eevee_vs_pikachu_battle_result),
            ('pikachu', 'eevee', pokemon_data.pikachu_vs_eevee_battle_result),
        ]
    )
    def test_ok(self, pokemon_name_1, pokemon_name_2, battle_result) -> None:
        # arrange & act
        with requests_mock.mock() as m:
            m.get(
                f'https://pokeapi.co/api/v2/pokemon/eevee',
                json=pokemon_data.eevee_data,
            )
            
            m.get(
                f'https://pokeapi.co/api/v2/pokemon/pikachu',
                json=pokemon_data.pikachu_data,
            )
            
            response = client.get(f"/pokemon_battle/{pokemon_name_1}/vs/{pokemon_name_2}")

        # assert
        assert response.status_code == 200
        assert response.json() == battle_result
