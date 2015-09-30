import os

# sqlacodegen  mysql://root:r@@t@locahost/mydb --outfile mysql_db
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'This string will be replaced with a proper key in production.'

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/etldb"
DATABASE_CONNECT_OPTIONS = {}

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"


WORKING_DIR = '../data/working'
ARCHIVE_DIR = '../data/archive'
