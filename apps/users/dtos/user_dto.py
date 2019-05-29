from dataclasses import dataclass


@dataclass
class CreateUserDto:
    email: str = None
    password1: str = None
    password2: str = None
    nickname: str = None
    gender: str = None
    join_type: str = None


@dataclass
class UpdateUserDto:
    password: str = None
    target_field: str = None
    value: str = None


@dataclass
class LoginDto:
    email: str = None
    password: str = None
    join_type: str = None


@dataclass
class UserListDto:
    offset: int = None
    limit: int = None


@dataclass
class UpdateUserStateDto:
    token: str = None
    user_id: int = None
