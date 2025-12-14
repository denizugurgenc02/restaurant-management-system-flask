from typing import Any, List

from flaskr.domains.user.repositories import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository

    def get_by_id(self, user_id: int) -> Any | None:
        user = self.repository.get_by_id(user_id=user_id)

        if user is None:
            return None
        return user.serialize

    def list_users(self) -> List:
        users = self.repository.get_all()
        return [user.serialize for user in users]

    def create_new_user(self, name: str, email: str):

        try:
            new_user = self.repository.add(name, email)
            return new_user.serialize
        except Exception as e:
            print(e)
