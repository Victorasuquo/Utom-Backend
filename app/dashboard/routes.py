from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/", methods=["GET"])
@jwt_required()
def get_dashboard():
    user_identity = get_jwt_identity()
    role = user_identity["role"]

    buttons = ["Todo", "Chats", "Screens", "Meet", "Ideas", "Files"]
    if role == "admin":
        buttons += ["Build", "Marketing"]

    return jsonify({"dashboard": buttons}), 200
