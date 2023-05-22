from litestar.contrib.sqlalchemy.plugins.init import (
    SQLAlchemyAsyncConfig,
    SQLAlchemyInitPlugin,
)

sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string="postgresql+asyncpg://myuser:mypass@localhost:5432/mypg",
)
sqlalchemy_plugin = SQLAlchemyInitPlugin(config=sqlalchemy_config)
