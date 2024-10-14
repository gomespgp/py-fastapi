import contextlib
from typing import Any

from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.engine.base import RootTransaction
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
    Session
)


class Base(DeclarativeBase):
    pass


class DatabaseSessionManager:
    def __init__(self, host: str, engine_kwargs: dict[str, Any] = None):
        self._engine = create_engine(host, **engine_kwargs)
        self._session_maker = sessionmaker(bind=self._engine, expire_on_commit=True)

    @contextlib.contextmanager
    def connect(self) -> RootTransaction:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        with self._engine.begin() as connection:
            try:
                return connection
            except Exception:
                connection.rollback()
                raise

    def session(self) -> Session:
        if self._session_maker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._session_maker()
        try:
            return session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


sessionmanager = DatabaseSessionManager(settings.database_url, {"echo": settings.echo_sql})


def get_db_session():
    return sessionmanager.session()
