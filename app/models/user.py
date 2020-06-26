from app import db,ms
from flask_login import UserMixin
from werkzeug.security import check_password_hash


class UserRoles(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


class Roles(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))

    def __repr__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100),unique=True,nullable=False)
    password = db.Column(db.String(200),nullable=True)
    roles = db.relationship('Roles', secondary="user_roles", backref="users")

    @classmethod
    def from_credential(cls, email, password):
        user = cls.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                return user
        return None

    def __repr__(self):
        return self.email


class SerializerUser(ms.ModelSchema):
    class Meta:
        model = User




