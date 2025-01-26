from flask import Blueprint, request, jsonify
from app.extensions import mongo
from flask_jwt_extended import jwt_required, get_jwt_identity

onboarding_bp = Blueprint("onboarding", __name__)

@onboarding_bp.route("/complete", methods=["POST"])
@jwt_required()
def complete_onboarding():
    user_identity = get_jwt_identity()
    data = request.json
    required_fields = ["first_name", "last_name", "display_name", "role"]

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Missing required fields"}), 400

    mongo.db.users.update_one(
        {"email": user_identity["email"]},
        {"$set": {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "display_name": data["display_name"],
            "role": data["role"]
        }},
    )
    return jsonify({"message": "Onboarding completed"}), 200
