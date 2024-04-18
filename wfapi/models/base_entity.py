from sqlalchemy import Integer, Column, Boolean, DateTime, func
from wfapi.db_config.db_setup import Base

class BaseEntity(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_on = Column(DateTime, default=func.now())
    updated_on = Column(DateTime, default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, default=True)