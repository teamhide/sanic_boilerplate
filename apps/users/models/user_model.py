from core.databases import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(2), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    is_block = db.Column(db.Boolean, default=False)
