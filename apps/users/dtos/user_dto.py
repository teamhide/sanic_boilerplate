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
