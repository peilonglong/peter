def get_database_uri(dbinfo):
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    user = dbinfo.get("USER") or "root"
    password = dbinfo.get("PASSWORD") or "123456"
    db = dbinfo.get("DB") or "mydb"
    type = dbinfo.get("TYPE") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"
    encoding = dbinfo.get("ENCODING") or "utf8"
    return '{}+{}://{}:{}@{}:{}/{}?charset={}'.format(type,driver,user,password,host,port,db,encoding)


class Config:
    DEBUG = True
    TESTTING = True
    SECRET_KEY = 'abcxyz'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DevelopConfig(Config):
    TESTTING = False

    DATABASE = {
        'HOST':'localhost',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'123456',
        'DB':'mydb',
        'TYPE':'mysql',
        'DRIVER':'pymysql',
        'ENCODING':'utf8',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class TestingConfig(Config):
    DEBUG = False

    DATABASE = {
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'DB': 'rest',
        'TYPE': 'mysql',
        'DRIVER': 'pymysql',
        'ENCODING': 'utf8',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

class ProductConfig(Config):
    DEBUG = False
    TESTTING = False

    DATABASE = {
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'DB': 'mydb',
        'TYPE': 'mysql',
        'DRIVER': 'pymysql',
        'ENCODING': 'utf8',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


config = {
    'develop': DevelopConfig,
    'test': TestingConfig,
    'product':ProductConfig,
    'default':DevelopConfig,
}

