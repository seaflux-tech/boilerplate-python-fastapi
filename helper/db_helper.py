from config.db_config import engine
from models.user_model import user

class DBHelper:
    def execute_query(query):
        with engine.connect() as db:
            result = db.execute(query)
            db.commit()
            return result
    
    def get_user_by_email(email: str):
        helper = DBHelper.execute_query(user.select().where(user.c.email == email)).fetchone()
        return helper      

    def get_user_by_id(id: int):
        return DBHelper.execute_query(user.select().where(user.c.id == id)).fetchone()
    
    