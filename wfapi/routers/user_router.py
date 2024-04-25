from datetime import timedelta
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Form
from starlette import status

from wfapi.enums.role import Role
from wfapi.logger_config.logger import logger
from wfapi.models import app_user
from wfapi.models.app_user import AppUser
from wfapi.queries import app_user_queries
from wfapi.schemas.sign_up_req import SignUpReq
from sqlalchemy.orm import Session
from wfapi.db_config.db_setup import get_db
from wfapi.utility.utility import create_access_token, login_response, apiResponse, verify

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/sign-up")
async def signUpUser(request: SignUpReq, db: Session = Depends(get_db)):
    print("Started.......")
    existing_user = app_user_queries.findUserByEmail(request.email, db)
    print("Started.......1")
    if existing_user:
        logger.error("Email already exists")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    # # Create a new user
    new_user = app_user.saveAppUser(request, Role.CLIENT)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(
        data={
            "id": new_user.id,
            "email": new_user.email,
            "role": new_user.role,
        },
        expires_delta=timedelta(minutes=90),
    )
    logger.info("User signed up successfully")
    return login_response(access_token, new_user.email, new_user.role, new_user.id)

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):

    logger.info("Starting login process...")
    appUser = app_user_queries.findUserByEmail(username, db)

    if appUser is not None and appUser.is_active == False:
        return apiResponse(HTTPStatus.FORBIDDEN, "ERROR")
    if appUser is None:
        return apiResponse(HTTPStatus.UNAUTHORIZED, "ERROR")
    if not verify(password, appUser.password):
        return apiResponse(HTTPStatus.UNAUTHORIZED, "PASSWORD")
    if appUser.email == username:
        logger.info("Generating access token")
        acess_token = create_access_token(
            data={
                "id": appUser.id,
                "email": appUser.email,
                "role": appUser.role,
            },
            expires_delta=timedelta(minutes=90),
        )
        return login_response(acess_token, appUser.email, appUser.role, appUser.id)
    else:
        logger.error("Invalid Enter valid credentials")
        return apiResponse(HTTPStatus.NOT_FOUND, "ERROR")