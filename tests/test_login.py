import pytest
from httpx import AsyncClient
from restapi.conf_test_db import app


class TestLogin:
    def setup(self):
        self.client = AsyncClient(app=app, base_url="http://test")
        self.user_data = {
            "username": "test@gmail.com",
            "password": "password",
        }

    @pytest.mark.asyncio
    async def test_login(self):

        async with self.client as ac:
            response = await ac.post(
                "/login",
                data={
                    "username": "test@gmail.com",
                    "password": "password",
                },
            )
            assert response.status_code == 200

            response = await ac.post(
                "/login",
                data={
                    "username": "test2@gmail.com",
                    "password": "password",
                },
            )
            assert response.status_code == 400

            response = await ac.post(
                "/login",
                data={
                    "username": "test@gmail.com",
                    "password": "password1",
                },
            )
            assert response.status_code == 400
