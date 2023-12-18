# Importing libraries
from dtos.auth_dto import LoginResponseModel, LoginRequest
from dtos.user_dto import UserModel
from helper.token_helper import TokenHelper
from helper.hashing import Hash
from helper.api_helper import APIHelper

class AuthController:
    def login(request: LoginRequest) -> LoginResponseModel:
        user = Hash.authenticate_user(
            username=request.username, password=request.password)
        access_token = TokenHelper.create_access_token(
            data={"id": user.id}
        )
        response = LoginResponseModel(
            user=UserModel(**user.__dict__),
            token=access_token,
        )
        return APIHelper.send_success_response(
            data=response,successMessageKey='translation.SUCCESS'
        )
        
