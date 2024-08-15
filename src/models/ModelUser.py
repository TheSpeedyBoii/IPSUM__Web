from .entities.User import User

class ModelUser():

    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT user_id, email, password FROM users WHERE email = '{}'""".format(user.email)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def get_by_id(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT user_id, first_name, email FROM users WHERE user_id = '{}'""".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return User(row[0], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)