from flask import jsonify, request
from flask.views import MethodView

from flaskr.domains.user.repositories import UserRepository
from flaskr.domains.user.services import UserService

from . import bp

user_repo = UserRepository()
user_service = UserService(user_repository=user_repo)


class UserListAPI(MethodView):

    def get(self):
        users_data = user_service.list_users()
        return jsonify(users_data)

    def post(self):
        data = request.get_json()

        if not data or "name" not in data or "email" not in data:
            return jsonify({"error": "empty or wrong data."}), 400

        try:
            new_user = user_service.create_new_user(
                name=data["name"], email=data["email"]
            )
            return jsonify(new_user), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 409  # Conflict
        except Exception:
            return jsonify({"error": "Unknow error"}), 500


class UserDetailAPI(MethodView):
    def get(self, user_id: int):
        user = user_service.get_by_id(user_id=user_id)
        return jsonify(user)


bp.add_url_rule(
    "/", view_func=UserListAPI.as_view("user_list_api"), methods=["GET", "POST"]
)

bp.add_url_rule(
    "/<int:user_id>",
    view_func=UserDetailAPI.as_view("user_detail_api"),
    methods=["GET"],
)
