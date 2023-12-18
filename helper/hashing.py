from passlib.context import CryptContext
from dtos.user_dto import UserModel
from helper.db_helper import DBHelper
from helper.api_helper import APIHelper
hash_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def get_hash(text: str):
        return hash_context.hash(text)

    def verify(plain_text: str, hashed_text: str):
        return hash_context.verify(plain_text, hashed_text)

    def authenticate_user(username: str, password: str) -> UserModel:
        user = DBHelper.get_user_by_email(username)
        password = Hash.verify(password, user.password) if user else False
        if user and password :
            return UserModel(**user._mapping)
        return APIHelper.send_unauthorized_error(errorMessageKey='translation.INVALID_CREDENTIAL')
        