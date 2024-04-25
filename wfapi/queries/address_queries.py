from wfapi.models import address
from sqlalchemy import func
from sqlalchemy.orm import Session


def findUserByAppUserIdAndIsPrimary(id: int, db: Session):
    print("test....")
    address_test = db.query(address.Address).filter(
        address.Address.app_user_id == id,
        address.Address.is_primary == True
    ).first()
    return address_test