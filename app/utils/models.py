from flask_restful import marshal
from sqlalchemy.ext.declarative import declared_attr

from ..components import db


class HasId:
    """Mixin adding id primary key to the table"""
    @declared_attr
    def id(cls):
        return db.Column(db.Integer, primary_key=True)


class Serializable:
    """Mixin adding serialize() method to models"""

    def serialize(self, attribute='structure'):
        """Serialize object using the structure.
        Params:
            attribute (string):
                The field name where the structure is stored.
        """
        return dict(marshal(self, getattr(self, attribute)))
