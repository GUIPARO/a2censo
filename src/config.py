class DevelopmentConfig():
    DEBUG = True 
    MYSQL_HOST= '127.0.0.1'
    MYSQL_USER= 'root'
    MYSQL_PASSWORD= '1234'
    MYSQL_DB = 'a2censo'
    MYSQL_PORT = '4550'


config = {
    'development' : DevelopmentConfig
}