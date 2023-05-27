from litestar.contrib.sqlalchemy.base import UUIDBase
from sqlalchemy.orm import Mapped


class Whatever(UUIDBase):
    name: Mapped[str]

    class Config:
        orm_mode = True
