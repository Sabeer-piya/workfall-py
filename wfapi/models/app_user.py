from sqlalchemy import Integer, ForeignKey, String, Column, Float, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from base_entity import BaseEntity

class AppUser(BaseEntity):
    __table_name__ = "app_user"
    first_name = Column(String(255), index=True)
    second_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    phonenumber = Column(String, nullable=False)
    is_active = Column(String, nullable=False, default=True)
    role = Column(String)
    address = relationship("Address", back_populates="app_user")
