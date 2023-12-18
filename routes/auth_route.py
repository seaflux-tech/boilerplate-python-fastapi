# Importing libraries
from fastapi import APIRouter
from controllers.auth_controller import AuthController
from dtos.auth_dto import LoginRequest

# Declaring router
auth = APIRouter(tags=['Authentication'])

@auth.post('/login')
async def login(request: LoginRequest):
    return AuthController.login(request)