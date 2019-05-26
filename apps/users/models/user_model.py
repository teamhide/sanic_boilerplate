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

    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(2), nullable=False)
    join_type = db.Column(db.String(15), default='default')
    is_active = db.Column(db.Boolean, default=True)
    is_block = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
