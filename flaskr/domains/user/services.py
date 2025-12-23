from typing import Any, Dict, List

from flask import abort

from flaskr.domains.user.models import User
from flaskr.domains.user.repositories import UserRepository


class UserService:
    repository = UserRepository()

    def get_by_id(self, item_id: int) -> Any | None:
        user = self.repository.get_by_id(item_id=item_id)

        if user is None:
            abort(404, description="There is no user")

        response = user.serialize
        response["role"] = {"id": user.role.id, "name": user.role.name}
        return response

    def list_users(self) -> List:
        users = self.repository.get_all()
        return [user.serialize for user in users]

    def create_new_user(
        self,
        username: str = None,
        password: str = None,
        display_name: str = None,
        email: str = None,
        role_id: int = None,
    ) -> Dict | None:
        if existing_user := self.repository.get_by_username(username=username):
            abort(
                code=409,
                description=f"this user already current."
                f" detail: {existing_user.serialize}",
            )
        new_user = self.repository.add(
            User(
                username=username,
                password=password,
                display_name=display_name,
                email=email,
                role_id=role_id,
            )
        )
        user_id = new_user.serialize.get("id")
        if user_id:
            return self.get_by_id(item_id=user_id)

    def update_user(self, user_id: int, data: Dict) -> Dict | None:
        self.get_by_id(item_id=user_id)
        response = self.repository.update(item_id=user_id, data=data)
        if response:
            return self.get_by_id(item_id=user_id)

    def delete_user(self, user_id: int) -> bool:
        self.get_by_id(item_id=user_id)
        return self.repository.delete(item_id=user_id)
