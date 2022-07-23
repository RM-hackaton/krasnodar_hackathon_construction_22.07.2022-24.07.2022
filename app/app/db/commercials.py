import sqlalchemy
from sqlalchemy import ForeignKey

from .base import metadata

commercials = sqlalchemy.Table(
    "commercials",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("house_id", sqlalchemy.Integer, ForeignKey("houses.id")),
    sqlalchemy.Column("owner_id", sqlalchemy.Integer),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("floor", sqlalchemy.Integer),
    sqlalchemy.Column("square", sqlalchemy.Float),
    sqlalchemy.Column("price", sqlalchemy.Float),
    sqlalchemy.Column("price_meter", sqlalchemy.Float),
    sqlalchemy.Column("plan", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
)
