from asyncpg.pgproto import pgproto  # type: ignore
from litestar import Litestar
from litestar.serialization import DEFAULT_TYPE_ENCODERS

from guidstuff.database import sqlalchemy_plugin

app = Litestar(
    plugins=[sqlalchemy_plugin],
    type_encoders={**DEFAULT_TYPE_ENCODERS, pgproto.UUID: str},
    debug=True,
)
