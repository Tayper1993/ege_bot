from contextlib import asynccontextmanager

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()

async_engine = create_async_engine(
    'postgresql+asyncpg://scot:tiger@localhost:5432/mydatabase',
    poolclass=NullPool,
    future=True,
    connect_args={'statement_cache_size': 0},
)


def async_session_generator():
    return sessionmaker(
        async_engine,
        class_=AsyncSession,
    )


@asynccontextmanager
async def get_session():
    async with async_session_generator()() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
