from .. import db
from .. import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

registrations = db.Table('registrations',
                         db.Column('user_id', db.Integer,
                                   db.ForeignKey('user.id')),
                         db.Column('contrat_id', db.Integer,
                                   db.ForeignKey('contrat.id'))
                         )

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    users = db.relationship('User', backref='role')


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    mobile = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    firm_id = db.Column(db.Integer, db.ForeignKey('firm.id'))
    contrat = db.relationship('Contrat', secondary=registrations, backref=db.backref(
        'user', lazy='dynamic'), lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('password in not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
