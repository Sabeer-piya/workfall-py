from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from wfapi.enums.role import Role
from wfapi.logger_config.logger import logger
from wfapi.models.app_user import AppUser
from wfapi.queries import app_user_queries
from wfapi.schemas.sign_up_req import SignUpReq
from sqlalchemy.orm import Session
from wfapi.db_config.db_setup import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/sign-up")
async def signUpUser(request: SignUpReq, db: Session = Depends(get_db)):
    print("Started.......")
    existing_user = app_user_queries.findUserByEmail(request.email, db)
    print(existing_user)
    print("Started.......1")
    # if existing_user:
    #     logger.error("Email already exists")
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    #
    # # Create a new user
    new_user = AppUser(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=request.password,
        phonenumber=request.phone_number,
        role=Role.CLIENT  # Assuming all signups are for clients
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Return a success response
    return {"message": "User signed up successfully"}
