from .entities.User import User

class ModelUser():
    
    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT id, email, password, fullname FROM users where email ='{}'""".format(user.email)
            cursor.execute(sql)
            row=cursor.fetcone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password),row[3])
                return user
            else:
                return None
        except Exception as ex:
            return Exception(ex)