from sqlalchemy import Table, Column, Integer, String, DateTime
from datetime import datetime
from config.db_config import metadata

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("first_name", String),
    Column("last_name", String),
    Column("email", String),
    Column("password", String),
    Column("address", String),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow),
    extend_existing=True
)
