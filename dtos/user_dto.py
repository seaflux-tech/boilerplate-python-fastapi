from pydantic import BaseModel, validator
from helper.validation_helper import ValidationHelper
from datetime import datetime

class UserModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    address: str
    created_at: datetime
    updated_at: datetime
    
class CreateUserModel(BaseModel):
    first_name: str
    last_name: str
    address: str
    email: str
    password: str
    _email = validator("email", allow_reuse=True)(
        ValidationHelper.is_valid_email)
    _password = validator("password", allow_reuse=True)(
        ValidationHelper.is_valid_password)