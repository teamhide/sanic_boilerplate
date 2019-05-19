from apps.users.models import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    nickname = Column(String(20), nullable=False)
    gender = Column(String(2), nullable=False)
    is_active = Column(Boolean, default=False)
    is_block = Column(Boolean, default=False)
