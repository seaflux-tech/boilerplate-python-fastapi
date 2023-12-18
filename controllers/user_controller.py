from fastapi import HTTPException
from models.user_model import user
from helper.db_helper import DBHelper
from dtos.user_dto import CreateUserModel, UserModel
from helper.hashing import Hash
from helper.api_helper import APIHelper
from datetime import datetime
from dtos.base_dto import BaseResponseModel

class UserController:
    def get_users():
        all_users = DBHelper.execute_query(user.select()).fetchall()
        user_list = list(map(lambda users: UserModel(**users._mapping), all_users))
        return APIHelper.send_success_response(data=user_list, successMessageKey='translations.SUCCESS')

    def get_user(user_id: int):
        query = DBHelper.execute_query(user.select().where(user.c.id == user_id)).fetchone()
        if query:
            return APIHelper.send_success_response(data=UserModel(**query._mapping), successMessageKey='translation.SUCCESS')
        return APIHelper.send_error_response(errorMessageKey='translation.USER_DOES_NOT_EXIST')

    def create_user(user_data: CreateUserModel) -> BaseResponseModel:
        existing_user = DBHelper.execute_query(user.select().where(user.c.email == user_data.email)).fetchone()
        if existing_user:
            return APIHelper.send_error_response(errorMessageKey='translation.USER_ALREADY_EXIST')
        password = Hash.get_hash(user_data.password)
        new_user = DBHelper.execute_query(user.insert().values(
            first_name=user_data.first_name, last_name=user_data.last_name, address=user_data.address,
            email=user_data.email, password=password).returning(*user.c)).fetchone()
        return APIHelper.send_success_response(data=UserModel(**new_user._mapping), successMessageKey='translation.USER_CREATED')
        
    def update_user(user_id: int, user_data: CreateUserModel):
        existing_user = DBHelper.execute_query(user.select().where(user.c.id == user_id)).fetchone()
        if not existing_user:
            raise APIHelper.send_error_response(errorMessageKey='translation.USER_NOT_FOUND')
        if user_data.password and Hash.verify(user_data.password, existing_user.password):
            password = existing_user.password
        else:
            password = Hash.get_hash(user_data.password)
        updated_user = DBHelper.execute_query(user.update().where(user.c.id == user_id).values(first_name=user_data.first_name, last_name=user_data.last_name, address=user_data.address,
            email=user_data.email, password=password, updated_at=datetime.now()).returning(*user.c)).fetchone()
        return APIHelper.send_success_response(data=UserModel(**updated_user._mapping), successMessageKey='translation.USER_UPDATED')

    def delete_user(user_id: int):
        query = user.delete().where(user.c.id == user_id)
        result = DBHelper.execute_query(query)
        if result.rowcount == 0:
            raise APIHelper.send_error_response(errorMessageKey='translation.USER_NOT_FOUND')
        return APIHelper.send_success_response(successMessageKey='translation.USER_DELETED')