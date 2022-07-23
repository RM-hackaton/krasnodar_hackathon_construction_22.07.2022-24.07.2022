from .housing_complexes import housing_complexes
from .houses import houses
from .commercials import commercials
from .base import metadata, engine

metadata.create_all(bind=engine)
