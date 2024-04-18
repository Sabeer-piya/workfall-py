from sqlalchemy import Integer, ForeignKey, String, Column, Float, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from base_entity import BaseEntity


class Address(BaseEntity):
    __table_name__ = "address"
    address = Column(String(255), index=True)
    city = Column(String(255), index=True)
    State = Column(String(255), unique=True, index=True)
    country = Column(String(255))
    pincode = Column(String, nullable=False)
    is_primary = Column(String, nullable=False, default=True)
    app_user_id = Column(Integer, ForeignKey("app_user_id"))
    app_user = relationship("AppUser", back_populates="address")