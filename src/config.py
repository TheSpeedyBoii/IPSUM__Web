class Config:
    SECRET_KEY = 'B!1weNAt1T??kvhUI*S'


class DelevopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'db_system'


config = {
    'development': DelevopmentConfig
}