from datetime import timedelta, datetime
from typing import List
from fastapi import HTTPException, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import jwt
from sqlalchemy.orm import Session
from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def bcrypt(password: str):
    return pwd_cxt.hash(password)


def verify(plain_password, hashed_password):
    return pwd_cxt.verify(plain_password, hashed_password)


def apiResponse(responseCode=None, message=None, payload=None):
    return JSONResponse({'statusCode': responseCode, "message": message, 'payload': jsonable_encoder(payload)},
                        status_code=responseCode)


# def create_access_token(data: dict, expires_delta: timedelta):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update({'exp': expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


def login_response(access_token, user_email, role, id):
    return {
        "statusCode": 200,
        "message": status.HTTP_200_OK,
        "access_token": access_token,
        "token_type": "bearer",
        'user_id': id,
        "user_email": user_email,
        "role": role.upper()
    }


# async def get_current_user_role(request: Request, db: Session = Depends(get_db)):
#     try:
#         print("enter")
#         token = request.headers.get("Authorization", "").split("Bearer ")[1]
#         print(token)
#         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         print(decoded_token)
#         user_email = decoded_token.get("email")
#         if not user_email:
#             raise HTTPException(status_code=401, detail="Invalid token: No email found in payload")
#         user = findUserByUsername(user_email, db)
#         if not user:
#             raise HTTPException(status_code=401, detail="User not found")
#
#         return user.role  # or any other data you want to return
#
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token has expired")
#     except jwt.DecodeError:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
#
# class RoleChecker:
#     def __init__(self, allowed_roles: List):
#         self.allowed_roles = allowed_roles
#
#     def __call__(self, role: str = Depends(get_current_user_role)):
#         print("rolecheck" + role)
#         if role not in self.allowed_roles:
#             print(f"User with role {role} not in {self.allowed_roles}")
#             raise HTTPException(status_code=403, detail="Operation not permitted")
