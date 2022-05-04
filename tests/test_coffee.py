import pytest
from httpx import AsyncClient
from restapi.conf_test_db import app

from restapi.auth.jwt import create_access_token


class Testcoffee:
    def setup(self):
        self.client = AsyncClient(app=app, base_url="http://test")
        self.coffee_data = {
            "title": "latte",
            "description": "Latte Coffee",
            "price": 250,
            "image_url": "https://test.com/images/coffee.jpg",
        }
        self.user_access_token_good = create_access_token({"sub": "test@gmail.com", "stuff": True})

    @pytest.mark.asyncio
    async def test_get_all_coffee_bad(self):
        async with self.client as ac:
            response = await ac.get("/api/v1/coffee/")

        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_get_coffee_by_id_bad(self):
        async with self.client as ac:
            response = await ac.get("/api/v1/coffee/5/")

        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_create_coffee(self):
        async with self.client as ac:
            response = await ac.post(
                "/api/v1/coffee/",
                json=self.coffee_data,
                headers={"Authorization": f"Bearer {self.user_access_token_good}"},
            )
            assert response.status_code == 201

            response = await ac.post(
                "/api/v1/coffee/",
                json=self.coffee_data,
                headers={"Authorization": f"Bearer {self.user_access_token_good}"},
            )
            assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_get_all_coffee_success(self):
        async with self.client as ac:
            response = await ac.get("/api/v1/coffee/")

        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_get_coffee_by_id(self):
        async with self.client as ac:
            response = await ac.get("/api/v1/coffee/1/")

        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_delete_coffee_by_id(self):
        async with self.client as ac:
            response = await ac.delete(
                "/api/v1/coffee/1/", headers={"Authorization": f"Bearer {self.user_access_token_good}"}
            )
            assert response.status_code == 200
            assert response.json() == {"status": "coffee was deleted"}

            response = await ac.delete(
                "/api/v1/coffee/1/", headers={"Authorization": f"Bearer {self.user_access_token_good}"}
            )
            assert response.status_code == 404
