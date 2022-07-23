import sqlalchemy

from .base import metadata

housing_complexes = sqlalchemy.Table(
    "housing_complexes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("district", sqlalchemy.String),
    sqlalchemy.Column("min_square", sqlalchemy.Float),
    sqlalchemy.Column("min_price", sqlalchemy.Float),
    sqlalchemy.Column("complex_class", sqlalchemy.String),
    sqlalchemy.Column("address", sqlalchemy.String),
    sqlalchemy.Column("img", sqlalchemy.String),
)
