"""Default Settings"""

#----------------------------------------------------------------------------#
# DATABASE
#-------------#

# database
SQLALCHEMY_DATABASE_URI = 'sqlite:///elf.db'

#----------------------------------------------------------------------------#
# SERVER
#-------------#

HOST = '0.0.0.0'
PORT = 5000

# debug mode
DEBUG = True

SECRET_KEY = u'Gh\x00)\xad\x7fQx\xedvx\xfetS-\x9a\xd7\x17$\x08_5\x17F'
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = SECRET_KEY
