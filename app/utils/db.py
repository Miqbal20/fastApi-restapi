import sqlalchemy as sq
from app.config import config

db_engine = sq.create_engine(
    config.DB,
    pool_size=config.DB_POOL_SIZE,
    pool_pre_ping=config.DB_POOL_PRE_PING,
    pool_recycle=config.DB_POOL_RECYCLE,
    echo=config.DB_ECHO
)