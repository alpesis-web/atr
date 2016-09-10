"""API Server"""

from flask import Flask
from flask_security import SQLAlchemyUserDatastore
from flask_security.utils import encrypt_password

from utils.sqlalchemy import db
from utils.security import security

from apis.users.models.user import User, Role

from apis.index.index import blueprint as index
from apis.dreams.api import blueprint as dreams

def api_server(custom_settings=None):
   
    # init server 
    server = Flask(__name__)
    # init settings
    server.config.from_object('settings.default')
    server.config.from_envvar('SETTINGS', silent=True)
    server.config.from_object(custom_settings)

    # init db
    db.init_app(server)
    # init user
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(server, user_datastore)

    # import features
    server.register_blueprint(index)
    server.register_blueprint(dreams)

    # render context 
    with server.app_context():
        db.create_all()
        if not User.query.first():
            user_datastore.create_user(email='user@example.com',
                                       password=encrypt_password('user')) 
            db.session.commit()

    return server
