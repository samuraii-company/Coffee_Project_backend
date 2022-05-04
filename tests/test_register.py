import pytest
from httpx import AsyncClient
from restapi.conf_test_db import app


class TestRegister:
    def setup(self):
        self.client = AsyncClient(app=app, base_url="http://test")
        self.user_data = {"email": "test@gmail.com", "password": "password", "telegram_id": 123456}

    @pytest.mark.asyncio
    async def test_register(self):

        async with self.client as ac:
            response = await ac.post("/register", json=self.user_data)
            assert response.status_code == 201

            response = await ac.post("/register", json=self.user_data)
            assert response.status_code == 400
