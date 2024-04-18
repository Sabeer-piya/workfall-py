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
    status = Column(String, nullable=False, default=UserStatus.ACTIVE)
    role = Column(String, nullable=False, default=UserRoleEnum.USER)
    cart = relationship("Cart", uselist=False, back_populates="user")
