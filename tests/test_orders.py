import pytest
from httpx import AsyncClient
from restapi.auth.jwt import create_access_token
from restapi.conf_test_db import app
from restapi.conf_test_db import override_get_db
from restapi.users import models
from restapi.coffee import models as coffee_models
from restapi.auth import hashing


class TestOrders:
    def setup(self):
        self.client = AsyncClient(app=app, base_url="http://test")
        self.database = next(override_get_db())
        self.new_user = models.Users(
            email="test222@gmail.com", password=hashing.get_password_hash("password"), telegram_id=13221, is_stuff=False
        )
        self.database.add(self.new_user)
        self.new_coffee = coffee_models.Coffee(
            title="latte",
            description="lattee description",
            price=100,
            image_url="https://test.com/images/coffee.jpg",
        )
        self.database.add(self.new_coffee)

        self.database.commit()
        self.database.refresh(self.new_user)
        self.database.refresh(self.new_coffee)

        self.user_access_token_good = create_access_token({"sub": "test@gmail.com", "stuff": True})
        self.user_access_token_bad = create_access_token({"sub": "test222@gmail.com", "stuff": False})

    def teardown(self):
        self.database.query(models.Users).filter(models.Users.id == self.new_user.id).delete()
        self.database.commit()

    @pytest.mark.asyncio
    async def test_get_all_orders_bad(self):
        async with self.client as ac:
            response = await ac.get(
                "/api/v1/orders/", headers={"Authorization": f"Bearer {self.user_access_token_good}"}
            )

            assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_get_order_by_id_bad(self):
        async with self.client as ac:
            response = await ac.get(
                "/api/v1/orders/1/", headers={"Authorization": f"Bearer {self.user_access_token_good}"}
            )

            assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_create_new_order_and_update_status(self):
        self.order_data = {
            "telegram_charge_id": "2076523459_535590856_108052",
            "payment_charge_id": "2a020b19-000f-5000-8000-12bf6af1050c",
            "client": self.new_user.id,
            "coffee": self.new_coffee.id,
            "order_number": 6821,
            "order_price": 400,
        }
        async with self.client as ac:
            response = await ac.post(
                "/api/v1/orders/",
                json=self.order_data,
                headers={"Authorization": f"Bearer {self.user_access_token_good}"},
            )
            assert response.status_code == 201

            response = await ac.get(
                "/api/v1/orders/", headers={"Authorization": f"Bearer {self.user_access_token_good}"}
            )
            assert response.status_code == 200

            response = await ac.get(
                "/api/v1/orders/1/", headers={"Authorization": f"Bearer {self.user_access_token_good}"}
            )
            assert response.status_code == 200
            assert response.json()["status"] == "PENDING"

            response = await ac.patch(
                "/api/v1/orders/1/",
                json={"status": "COMPLITED"},
                headers={"Authorization": f"Bearer {self.user_access_token_good}"},
            )
            assert response.status_code == 200

            response = await ac.get(
                "/api/v1/orders/1/", headers={"Authorization": f"Bearer {self.user_access_token_good}"}
            )
            assert response.status_code == 200

            assert response.json()["status"] == "COMPLITED"

            response = await ac.patch(
                "/api/v1/orders/12/",
                json={"status": "COMPLITED"},
                headers={"Authorization": f"Bearer {self.user_access_token_good}"},
            )
            assert response.status_code == 404

            response = await ac.get(
                "/api/v1/orders/1/", headers={"Authorization": f"Bearer {self.user_access_token_bad}"}
            )
            assert response.status_code == 401
