from wfapi.models import app_user
from sqlalchemy import func
from sqlalchemy.orm import Session


def findUserByEmail(email: str, db: Session):
    print("test....")
    # app_user_test = db.query(app_user.AppUser).filter(
    #     app_user.AppUser.email == email.lower(),
    #     app_user.AppUser.is_active == True
    # ).first()
    # print(app_user_test)
    return None

