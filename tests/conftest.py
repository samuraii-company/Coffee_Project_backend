import pytest

from restapi.users import models
from restapi.auth import hashing


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    """Fixture to execute asserts before and after a test is run"""

    from restapi.conf_test_db import override_get_db

    database = next(override_get_db())
    new_user = models.Users(
        email="test@gmail.com", password=hashing.get_password_hash("password"), telegram_id=1312321, is_stuff=True
    )
    database.add(new_user)
    database.commit()

    yield  # this is where the testing happens

    database.query(models.Users).delete()
    database.commit()
