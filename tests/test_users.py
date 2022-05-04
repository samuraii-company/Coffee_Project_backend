import pytest
from httpx import AsyncClient
from restapi.auth.jwt import create_access_token
from restapi.conf_test_db import app


class TestUsers:
    def setup(self):
        self.client = AsyncClient(app=app, base_url="http://test")
        self.user_access_token_good = create_access_token({"sub": "test@gmail.com", "stuff": True})

    @pytest.mark.asyncio
    async def test_get_all_users(self):
        async with self.client as ac:
            response = await ac.get(
                "/api/v1/users/", headers={"Authorization": f"Bearer {self.user_access_token_good}"}
            )

            assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_get_me(self):
        async with self.client as ac:
            response = await ac.get(
                "/api/v1/users/me/?q=1312321", headers={"Authorization": f"Bearer {self.user_access_token_good}"}
            )
            assert response.status_code == 200

            response = await ac.get(
                "/api/v1/users/me/?q=123456", headers={"Authorization": f"Bearer {self.user_access_token_good}"}
            )
            assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_user_existse(self):
        async with self.client as ac:
            response = await ac.get("/api/v1/users/user/exists/?q=1312321")
            assert response.status_code == 200
            assert response.json() is True

            response = await ac.get("/api/v1/users/user/exists/?q=123456")
            assert response.status_code == 200
            assert response.json() is False
