from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, user_id, email, password, first_name="") -> None:
        self.id = user_id
        self.email = email
        self.password = password
        self.name = first_name
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)