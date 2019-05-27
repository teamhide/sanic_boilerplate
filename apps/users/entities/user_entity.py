from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserEntity:
    id: int = None
    email: str = None
    password: str = None
    nickname: str = None
    gender: str = None
    join_type: str = None
    is_active: bool = True
    is_block: bool = False
    is_admin: bool = False
    created_at: datetime = None
    updated_at: datetime = None
