from pydantic import BaseModel
from dtos.user_dto import UserModel

class LoginRequest(BaseModel):
    username: str
    password: str
    
class LoginResponseModel(BaseModel):
    user: UserModel
    token: str
