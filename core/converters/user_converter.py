from . import Converter
from apps.users.models import User
from apps.users.entities import UserEntity


class UserInteractorConverter(Converter):
    def user_dto_to_entity(self, dto):
        return UserEntity(**dto.__dict__)


class UserRepositoryConverter(Converter):
    def user_model_to_entity(self, model: User) -> UserEntity:
        return self.model_to_entity(model=model, entity=UserEntity)

    def user_entity_to_model(self, entity: UserEntity) -> User:
        return self.entity_to_model(entity=entity, model=User)

    def user_entity_to_dict(self, entity: UserEntity) -> dict:
        return entity.__dict__
