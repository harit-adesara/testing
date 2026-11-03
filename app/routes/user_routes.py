from flask import Blueprint, g

from backend.app.middleware import login_required
from backend.app.services import user_service
from backend.app.services.auth_service import public_user
from backend.app.utils.responses import success_response

user_bp = Blueprint("users", __name__)


@user_bp.get("/me")
@login_required
def me():
    return success_response(public_user(g.current_user))


@user_bp.get("/")
@login_required
def list_all():
    return success_response(user_service.list_users())


@user_bp.get("/<int:user_id>")
@login_required
def get_one(user_id):
    return success_response(user_service.get_user(user_id))
