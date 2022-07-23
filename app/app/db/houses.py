import sqlalchemy
from sqlalchemy import ForeignKey

from .base import metadata

houses = sqlalchemy.Table(
    "houses",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("complex_id", sqlalchemy.Integer, ForeignKey("housing_complexes.id")),
    sqlalchemy.Column("liter", sqlalchemy.Integer),
    sqlalchemy.Column("parking", sqlalchemy.String),
    sqlalchemy.Column("finished", sqlalchemy.String),
)
