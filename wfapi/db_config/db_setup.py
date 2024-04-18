from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

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
        print("sql roll back exception")
        db_session.rollback()
    except Exception as ex:
        print(ex)
        db_session.rollback()
    finally:
        print("final closed")
        db_session.close()
