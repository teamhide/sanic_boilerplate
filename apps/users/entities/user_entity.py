from dataclasses import dataclass


@dataclass
class UserEntity:
    email: str = None
    password: str = None
    nickname: str = None
    gender: str = None
    join_type: str = None
    is_active: bool = True
    is_block: bool = False
    is_admin: bool = False
