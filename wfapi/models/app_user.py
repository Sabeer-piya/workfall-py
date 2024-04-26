from sqlalchemy import String, Column, Boolean
from sqlalchemy.orm import relationship

from wfapi.models.base_entity import BaseEntity
from wfapi.enums.role import Role
from wfapi.schemas.sign_up_req import SignUpReq
from wfapi.utility.utility import bcrypt
from wfapi.db_config.db_setup import Base


class AppUser(BaseEntity):
    __tablename__ = "app_user"
    first_name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    phonenumber = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)  # Corrected column type
    role = Column(String)
    address = relationship("Address", back_populates="app_user")
    bank_detail = relationship("BankDetail", back_populates="app_user")


def saveAppUser(request: SignUpReq, role: Role):
    return AppUser(
        first_name=request.first_name,
        last_name = request.last_name,
        email=request.email.lower(),
        password=bcrypt(request.password),
        phonenumber=request.phone_number,
        role=role,
    )