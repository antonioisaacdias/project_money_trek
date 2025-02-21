from database import db
from uuid import uuid4
from flask_login import UserMixin
from datetime import datetime
from enum import Enum

class RoleEnum(Enum):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(14), nullable=False, index=True, unique=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    role = db.Column(db.String(20), nullable=False, default=RoleEnum.USER.value)
    corp_id = db.Column(db.String(36), db.ForeignKey('corporations.id'), nullable=False)

    corporation = db.relationship('Corporation', back_populates='users')

    @property
    def role_enum(self):
        return RoleEnum(self.role)

    @role_enum.setter
    def role_enum(self, role: RoleEnum):
        self.role = role.value
