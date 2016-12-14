from flask_restful import fields

from app.components import db
from app.utils.models import HasId, Serializable

class AdminUser(HasId, Serializable, db.Model):
    __tablename__ = 'admin_user'

    email = db.Column(db.String(127), unique=True, index=True, nullable=False)
    password = db.Column(db.String(127), nullable=False)

    structure = {
        'id': fields.Integer,
        'email': fields.String,
        'password': fields.String,
    }

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
