from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
import os

# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())

# SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db" #consider using postgresql database in the future
SQLALCHEMY_DATABASE_URL = os.environ["cockroack_db_deta_connect_string"]

# SQLALCHEMY_DATABASE_URL = URL.create(
#     # "cockroachdb+asyncpg",
#     "cockroachdb",
#     username="james_neurocast_nl",
#     password=os.environ["cockroack_db_connect_string"],
#     host="free-tier13.aws-eu-central-1.cockroachlabs.cloud",
#     port=26257,
#     database="maple-coder-1764.defaultdb",
#     query={"disable_cockroachdb_telemetry": "True"},
# )

engine = create_engine(SQLALCHEMY_DATABASE_URL, 
                    #    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(
#     engine, expire_on_commit=False, class_=AsyncSession
# )

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()