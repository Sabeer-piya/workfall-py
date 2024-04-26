from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from wfapi.models.base_entity import BaseEntity


class BankDetail(BaseEntity):
    __tablename__ = "bank_detail"
    name = Column(String(255), index=True)
    ifscNumber = Column(String(255), index=True)
    address = Column(String(255), unique=True, index=True)
    pincode = Column(String(255))
    city = Column(String, nullable=False)
    country = Column(String(255), nullable=False, default=True)
    app_user_id = Column(Integer, ForeignKey("app_user.id"))
    app_user = relationship("AppUser", back_populates="bank_detail")