DB_USER = 'jm_admin'
DB_PASSWORD = ''
DB_HOST = ''
DB_DB = 'jm_db'

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB