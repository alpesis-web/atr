from flask_security import RoleMixin, UserMixin

from utils.sqlalchemy import db


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)


class Role(db.Model, RoleMixin):

    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String) 


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    active = db.Column(db.Boolean)

    roles = db.relationship('Role', secondary=roles_users,
                                    backref=db.backref('users', lazy='dynamic'))
