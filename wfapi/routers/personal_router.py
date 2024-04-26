from fastapi import APIRouter, Depends, HTTPException, Request
from starlette import status

from wfapi.enums.role import Role
from wfapi.logger_config.logger import logger
from wfapi.models.address import Address
from wfapi.models.app_user import AppUser
from wfapi.models.bank_details import BankDetail
from wfapi.queries import app_user_queries, address_queries
from wfapi.schemas.address_req import AddressReq
from sqlalchemy.orm import Session
from wfapi.db_config.db_setup import get_db
from wfapi.utility import utility
from wfapi.utility.utility import RoleChecker

router = APIRouter(prefix="/personal", tags=["Personal"])


@router.post("/save-address", dependencies=[Depends(RoleChecker([Role.CLIENT]))])
async def saveAddress(request: AddressReq, session: Request, db: Session = Depends(get_db)):
    existing_user = utility.get_current_user(session, db)
    if request.is_primary:
        old_address = address_queries.findUserByAppUserIdAndIsPrimary(existing_user.id)
        if old_address:
            logger.error("Updating primary address")
            old_address.is_primary = False
            db.add(old_address)
            db.commit()
            db.refresh(old_address)

    # Create a new user
    address = Address(
        address=request.address,
        city=request.city,
        State=request.State,
        country=request.country,
        pincode=request.pincode,
        is_primary=request.is_primary,
        app_user_id=existing_user.id,
    )
    db.add(address)
    db.commit()
    db.refresh(address)

    # Return a success response
    return {"message": "Address saved successfully"}

@router.post("/save-bank_details", dependencies=[Depends(RoleChecker([Role.CLIENT]))])
async def saveBankDetails(request: AddressReq, session: Request, db: Session = Depends(get_db)):
    existing_user = utility.get_current_user(session, db)

    # Create a new user
    bank_details = BankDetail(
        address=request.address,
        city=request.city,
        State=request.State,
        country=request.country,
        pincode=request.pincode,
        is_primary=request.is_primary,
        app_user_id=existing_user.id,
    )
    db.add(bank_details)
    db.commit()
    db.refresh(bank_details)

    # Return a success response
    return {"message": "Address saved successfully"}