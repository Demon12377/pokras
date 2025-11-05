from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pokras.config import AppConfig, Paths

engine = create_engine(
    f"sqlite:///{Paths.SQLITE_DB}",
    echo=AppConfig.VERBOSE_DB,
    query_cache_size=1200,
)

Session = sessionmaker(
    binds={
        # TODO: Add tables here
    },
    autoflush=True,
    expire_on_commit=False,
    bind=engine,
)
