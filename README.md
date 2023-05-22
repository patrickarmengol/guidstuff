## postgres docker container creation and startup

```
docker run --name=postgres -d -e POSTGRES_USER=myuser -POSTGRES_PASSWORD=mypass -e POSTGRES_DB=mypg -p 5432:5432 postgres:latest
```

## db url

```
postgresql+asyncpg://myuser:mypass@localhost:5432/mypg
```

## alembic cmd

```
alembic revision -m "create whatever table" --autogenerate
```
