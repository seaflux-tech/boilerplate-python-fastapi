from fastapi import APIRouter, Depends
from controllers.user_controller import UserController
from helper.token_helper import TokenHelper
from dtos.user_dto import UserModel, CreateUserModel

user = APIRouter(tags=['User'])

@user.get("/users")
def get_all_users(current_user: UserModel = Depends(TokenHelper.get_current_user)):
    return UserController.get_users()

@user.get("/user/{user_id}")
def get_user(user_id: int, current_user: UserModel = Depends(TokenHelper.get_current_user)):
    return UserController.get_user(user_id)

@user.post("/user")
def create_user(user_data: CreateUserModel, current_user: UserModel = Depends(TokenHelper.get_current_user)):
    return UserController.create_user(user_data)

@user.put("/user/{user_id}")
def update_user( user_id: int, user_data: CreateUserModel, current_user: UserModel = Depends(TokenHelper.get_current_user)):
    return UserController.update_user(user_id, user_data)

@user.delete("/user/{user_id}")
def delete_user(user_id: int, current_user: UserModel = Depends(TokenHelper.get_current_user)):
    return UserController.delete_user(user_id)
