import pytest
from unittest.mock import Mock
from fastapi import HTTPException
from fastapi.testclient import TestClient

from pokemon import enums
from pokemon import schema
from pokemon.pokeapi import exceptions as pokeapi_exc
from pokemon.app import create_app

app = create_app()
client = TestClient(app)

class TestApiPokemonCard:
    _pokemon_card = schema.PokemonCard(
        name='charizard',
        height=17,
        weight=905,
        stats=[
            schema.Stat(
                details=schema.StatDetails(name=enums.Stat.HP.value),
                base_stat=78,
            ),
            schema.Stat(
                details=schema.StatDetails(name=enums.Stat.ATTACK.value),
                base_stat=84,
            ),
            schema.Stat(
                details=schema.StatDetails(name=enums.Stat.DEFENSE.value),
                base_stat=78,
            ),
            schema.Stat(
                details=schema.StatDetails(name=enums.Stat.SPECIAL_ATTACK.value),
                base_stat=109,
            ),
            schema.Stat(
                details=schema.StatDetails(name=enums.Stat.SPECIAL_DEFENSE.value),
                base_stat=85,
            ),
            schema.Stat(
                details=schema.StatDetails(name=enums.Stat.SPEED.value),
                base_stat=100,
            ),
        ]
    )

    def test_ok(self, monkeypatch) -> None:
        # arrange
        pokemon_card_mock = Mock(
            return_value=self._pokemon_card,
        )
        monkeypatch.setattr(
            'pokemon.service.get_pokemon_card',
            pokemon_card_mock,
        )
        
        # act
        response = client.get(f"/pokemon_card/charizard")

        # assert
        assert response.status_code == 200
        assert response.json() == {
            'name': 'charizard', 
            'height': 17, 
            'weight': 905, 
            'stats': [
                {'details': {'name': 'hp'}, 'base_stat': 78}, 
                {'details': {'name': 'attack'}, 'base_stat': 84}, 
                {'details': {'name': 'defense'}, 'base_stat': 78}, 
                {'details': {'name': 'special-attack'}, 'base_stat': 109}, 
                {'details': {'name': 'special-defense'}, 'base_stat': 85}, 
                {'details': {'name': 'speed'}, 'base_stat': 100}
            ]
        }
    

    def test_server_error_raises_http_exception(self, monkeypatch) -> None:
        # arrange
        pokemon_card_mock = Mock(
            side_effect=pokeapi_exc.ServerError,
        )

        monkeypatch.setattr(
            'pokemon.service.get_pokemon_card',
            pokemon_card_mock,
        )
        
        # act
        response = client.get(f"/pokemon_card/charizard")

        # assert
        assert response.status_code == 503
        assert response.json().get('detail') == "Provider's service is unavailable"

    
    def test_client_error_raises_http_exception(self, monkeypatch) -> None:
        # arrange
        pokemon_card_mock = Mock(
            side_effect=pokeapi_exc.ClientError,
        )

        monkeypatch.setattr(
            'pokemon.service.get_pokemon_card',
            pokemon_card_mock,
        )
        
        # act
        response = client.get(f"/pokemon_card/charizard")

        # assert
        assert response.status_code == 500
        assert response.json().get('detail') == "Failed to execute remote request"
    

    def test_validation_error_raises_http_exception(self, monkeypatch) -> None:
        # arrange
        pokemon_card_mock = Mock(
            side_effect=pokeapi_exc.ValidationError,
        )

        monkeypatch.setattr(
            'pokemon.service.get_pokemon_card',
            pokemon_card_mock,
        )
        
        # act
        response = client.get(f"/pokemon_card/charizard")

        # assert
        assert response.status_code == 500
        assert response.json().get('detail') == "Failed to execute remote request"


    def test_raises_resource_not_found(self, monkeypatch) -> None:
        # arrange
        pokemon_card_mock = Mock(
            side_effect=pokeapi_exc.ResourceNotFound,
        )

        monkeypatch.setattr(
            'pokemon.service.get_pokemon_card',
            pokemon_card_mock,
        )
        
        # act
        response = client.get(f"/pokemon_card/random")

        # assert
        assert response.status_code == 404
        assert response.json().get('detail') == "Pokemon name: random"

class TestApiPokemonCard:
    _pokemon_battle = schema.BattleResult(
        pokemon_1=schema.PokemonCard(
            name='eevee',
            height=3,
            weight=65,
            stats=[ 
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.HP.value),
                    base_stat=55,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.ATTACK.value),
                    base_stat=55,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.DEFENSE.value),
                    base_stat=50,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.SPECIAL_ATTACK.value),
                    base_stat=45,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.SPECIAL_DEFENSE.value),
                    base_stat=65,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.SPEED.value),
                    base_stat=55,
                ),
            ]
        ),
        pokemon_2=schema.PokemonCard(
            name='pikachu',
            height=4,
            weight=60,
            stats=[ 
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.HP.value),
                    base_stat=35,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.ATTACK.value),
                    base_stat=55,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.DEFENSE.value),
                    base_stat=40,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.SPECIAL_ATTACK.value),
                    base_stat=50,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.SPECIAL_DEFENSE.value),
                    base_stat=50,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.SPEED.value),
                    base_stat=90,
                ),
            ]
        ),
        winner=schema.PokemonCard(
            name='pikachu',
            height=4,
            weight=60,
            stats=[ 
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.HP.value),
                    base_stat=35,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.ATTACK.value),
                    base_stat=55,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.DEFENSE.value),
                    base_stat=40,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.SPECIAL_ATTACK.value),
                    base_stat=50,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.SPECIAL_DEFENSE.value),
                    base_stat=50,
                ),
                schema.Stat(
                    details=schema.StatDetails(name=enums.Stat.SPEED.value),
                    base_stat=90,
                ),
            ]
        ),
        message="Battle is over, winner is pikachu",
    )

    def test_ok(self, monkeypatch) -> None:
        # arrange
        pokemon_battle_mock = Mock(
            return_value=self._pokemon_battle,
        )
        monkeypatch.setattr(
            'pokemon.service.perform_pokemon_battle',
            pokemon_battle_mock,
        )
        
        # act
        response = client.get(f"/pokemon_battle/eevee/vs/pikachu")

        # assert
        assert response.status_code == 200
        assert response.json() == {
            'pokemon_1': {
                'name': 'eevee', 
                'height': 3, 
                'weight': 65, 
                'stats': [
                    {'details': {'name': 'hp'}, 'base_stat': 55}, 
                    {'details': {'name': 'attack'}, 'base_stat': 55}, 
                    {'details': {'name': 'defense'}, 'base_stat': 50}, 
                    {'details': {'name': 'special-attack'}, 'base_stat': 45}, 
                    {'details': {'name': 'special-defense'}, 'base_stat': 65}, 
                    {'details': {'name': 'speed'}, 'base_stat': 55}
                ]
            }, 
            'pokemon_2': {
                'name': 'pikachu', 
                'height': 4, 
                'weight': 60, 
                'stats': [
                    {'details': {'name': 'hp'}, 'base_stat': 35}, 
                    {'details': {'name': 'attack'}, 'base_stat': 55}, 
                    {'details': {'name': 'defense'}, 'base_stat': 40}, 
                    {'details': {'name': 'special-attack'}, 'base_stat': 50}, 
                    {'details': {'name': 'special-defense'}, 'base_stat': 50}, 
                    {'details': {'name': 'speed'}, 'base_stat': 90}
                ]
            }, 
            'winner': {
                'name': 'pikachu', 
                'height': 4, 
                'weight': 60, 
                'stats': [
                    {'details': {'name': 'hp'}, 'base_stat': 35}, 
                    {'details': {'name': 'attack'}, 'base_stat': 55}, 
                    {'details': {'name': 'defense'}, 'base_stat': 40}, 
                    {'details': {'name': 'special-attack'}, 'base_stat': 50}, 
                    {'details': {'name': 'special-defense'}, 'base_stat': 50}, 
                    {'details': {'name': 'speed'}, 'base_stat': 90}
                ]
            }, 
            'message': 'Battle is over, winner is pikachu'
        }

    
    def test_server_error_raises_http_exception(self, monkeypatch) -> None:
        # arrange
        pokemon_battle_mock = Mock(
            side_effect=pokeapi_exc.ServerError,
        )

        monkeypatch.setattr(
            'pokemon.service.perform_pokemon_battle',
            pokemon_battle_mock,
        )
        
        # act
        response = client.get(f"/pokemon_battle/eevee/vs/pikachu")

        # assert
        assert response.status_code == 503
        assert response.json().get('detail') == "Provider's service is unavailable"

    
    def test_client_error_raises_http_exception(self, monkeypatch) -> None:
        # arrange
        pokemon_battle_mock = Mock(
            side_effect=pokeapi_exc.ClientError,
        )

        monkeypatch.setattr(
            'pokemon.service.perform_pokemon_battle',
            pokemon_battle_mock,
        )
        
        # act
        response = client.get(f"/pokemon_battle/eevee/vs/pikachu")

        # assert
        assert response.status_code == 500
        assert response.json().get('detail') == "Failed to execute remote request"

    
    def test_validation_error_raises_http_exception(self, monkeypatch) -> None:
        # arrange
        pokemon_battle_mock = Mock(
            side_effect=pokeapi_exc.ValidationError,
        )

        monkeypatch.setattr(
            'pokemon.service.perform_pokemon_battle',
            pokemon_battle_mock,
        )
        
        # act
        response = client.get(f"/pokemon_battle/eevee/vs/pikachu")

        # assert
        assert response.status_code == 500
        assert response.json().get('detail') == "Failed to execute remote request"
    

    def test_raises_resource_not_found(self, monkeypatch) -> None:
        # arrange
        pokemon_battle_mock = Mock(
            side_effect=pokeapi_exc.ResourceNotFound(f'Pokemon name: random'),
        )

        monkeypatch.setattr(
            'pokemon.service.perform_pokemon_battle',
            pokemon_battle_mock,
        )
        
        # act
        response = client.get(f"/pokemon_battle/random/vs/pikachu")

        # assert
        assert response.status_code == 404
        assert response.json().get('detail') == "Pokemon name: random"
