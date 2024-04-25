from pydantic import BaseModel, Field


class AddressReq(BaseModel):
    address : str
    city : str
    State : str
    country : str
    pincode : str
    is_primary: bool = Field(default=False, description="Indicates if the address is the primary address")
