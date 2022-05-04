import pytest
from httpx import AsyncClient
from restapi.conf_test_db import app


class TestMainPage:
    def setup(self):
        self.client = AsyncClient(app=app, base_url="http://test")

    @pytest.mark.asyncio
    async def test_home_page(self):

        async with self.client as ac:
            response = await ac.get("/")
        assert response.status_code == 200
