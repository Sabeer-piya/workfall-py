from sqlalchemy import String, Column, Boolean
from sqlalchemy.orm import relationship

from wfapi.models.base_entity import BaseEntity


class AppUser(BaseEntity):
    __tablename__ = "app_user"
    name = Column(String(255), index=True)
    ifscNumber = Column(String(255), index=True)
    address = Column(String(255), unique=True, index=True)
    pincode = Column(String(255))
    city = Column(String, nullable=False)
    country = Column(String(255), nullable=False, default=True)