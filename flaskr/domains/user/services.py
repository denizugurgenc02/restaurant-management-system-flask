from typing import Any, Dict

from flask import abort

from flaskr.core.base.services import BaseService
from flaskr.domains.user.models import User
from flaskr.domains.user.repositories import UserRepository


class UserService(BaseService):
    repository: UserRepository
    repository = UserRepository()

    def get_by_id(self, item_id: int) -> Any | None:
        user = self.repository.get_by_id(item_id=item_id)

        if user is None:
            abort(404, description="There is no user")

        response = user.serialize
        response["role"] = {"id": user.role.id, "name": user.role.name}
        return response

    def create_new_user(
        self,
        username: str = None,
        password: str = None,
        display_name: str = None,
        email: str = None,
        role_id: int = None,
    ) -> Dict | None:
        return self.create_new_item(
            model_class=User,
            unique_key=username,
            stun_name="username",
            username=username,
            password=password,
            display_name=display_name,
            email=email,
            role_id=role_id,
        )
