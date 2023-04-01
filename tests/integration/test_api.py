from fastapi.testclient import TestClient

from pokemon.app import create_app

app = create_app()
client = TestClient(app)

class TestApi:
    def test_root_ok(self) -> None:
        # arrange & act
        response = client.get("/")

        # assert
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to the battle ϞϞ〈๑⚈ ․̫⚈๑〉"}
        