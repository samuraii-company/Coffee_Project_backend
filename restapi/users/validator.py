from typing import Optional

from sqlalchemy.orm import Session
from . import models


async def verify_telegram_id_exist(tg_id: int, database: Session) -> Optional[models.Users]:
    """Verifying email exist in database"""

    return database.query(models.Users).filter(models.Users.telegram_id == tg_id).first()
