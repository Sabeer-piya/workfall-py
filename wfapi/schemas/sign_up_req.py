from pydantic import BaseModel

class SignUpReq(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str
    phone_number: str
