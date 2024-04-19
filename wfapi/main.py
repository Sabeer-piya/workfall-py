from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from wfapi.routers import user_router
from wfapi.db_config.db_setup import Base, engine
from wfapi.models import base_entity, app_user, address

app = FastAPI()
app_user.Base.metadata.create_all(engine)
address.Base.metadata.create_all(engine)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(user_router.router)