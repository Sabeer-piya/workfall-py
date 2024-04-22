from sqlalchemy import create_engine

# Importing models to ensure they are registered with Base.metadata
import wfapi.models.app_user
import wfapi.models.address
import wfapi.models.base_entity
from wfapi.db_config.db_setup import Base, engine

# Setup the engine (the URL will depend on your database setup)

# Create all tables
Base.metadata.create_all(engine)
