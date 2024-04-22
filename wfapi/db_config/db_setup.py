from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from wfapi.db_config import config

settings = config.get_settings()
engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db_session = SessionLocal()
    try:
        print("Session opened")
        yield db_session
    except SQLAlchemyError as e:
        print("SQLAlchemy exception triggered, rolling back transaction")
        db_session.rollback()
        raise HTTPException(status_code=500, detail=str(e)) from e
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        db_session.rollback()
        # Re-raising as HTTPException ensures FastAPI can handle it appropriately
        raise HTTPException(status_code=500, detail=str(ex)) from ex
    finally:
        db_session.close()
        print("Session closed")
