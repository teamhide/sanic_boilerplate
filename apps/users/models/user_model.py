from datetime import datetime
from sqlalchemy import Sequence
from core.databases import db


class User(db.Model):
    __tablename__ = 'users'

    USER_JOIN_TYPE = (
        ('facebook', 'Facebook'),
        ('default', 'Default'),
        ('kakao', 'Kakao')
    )
    USER_GENDER_TYPE = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    id = db.Column(db.BigInteger(), Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(62), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(2), nullable=False)
    join_type = db.Column(db.String(15), default='default')
    is_active = db.Column(db.Boolean, default=True)
    is_block = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0))
    updated_at = db.Column(db.DateTime, default=datetime.now().replace(microsecond=0))
