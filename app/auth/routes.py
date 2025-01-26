from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.extensions import mongo
from app.auth.utils import verify_google_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/google-signin", methods=["POST"])
def google_signin():
    token = request.json.get("token")
    user_info = verify_google_token(token)
    if not user_info:
        return jsonify({"message": "Invalid Google token"}), 400

    user = mongo.db.users.find_one({"email": user_info["email"]})
    if not user:
        return jsonify({"message": "User not found"}), 404

    access_token = create_access_token(identity={"email": user["email"], "role": user["role"]})
    return jsonify({"access_token": access_token}), 200



# from flask import Blueprint, request, jsonify, redirect, url_for
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from app.extensions import mongo
# from app.auth.utils import exchange_google_code, get_user_info

# auth_bp = Blueprint("auth", __name__)

# @auth_bp.route("/google-signin", methods=["POST"])
# def google_signin():
#     """Handle Google OAuth 2.0 sign-in."""
#     code = request.json.get("code")  # Authorization code from frontend
#     if not code:
#         return jsonify({"message": "Authorization code is required"}), 400

#     # Exchange the code for an access token
#     token_response = exchange_google_code(code)
#     if not token_response:
#         return jsonify({"message": "Invalid authorization code"}), 400

#     # Retrieve user info using the access token
#     user_info = get_user_info(token_response["access_token"])
#     if not user_info:
#         return jsonify({"message": "Unable to retrieve user information"}), 400

#     # Check if user exists in the database
#     user = mongo.db.users.find_one({"email": user_info["email"]})
#     if not user:
#         # If user doesn't exist, prompt onboarding
#         return jsonify({"message": "User not found. Proceed to onboarding."}), 404

#     # Generate a JWT token
#     access_token = create_access_token(identity={"email": user["email"], "role": user["role"]})
#     return jsonify({"access_token": access_token}), 200


# @auth_bp.route("/onboarding", methods=["POST"])
# def onboarding():
#     """Handle user onboarding."""
#     data = request.json
#     email = data.get("email")
#     first_name = data.get("first_name")
#     last_name = data.get("last_name")
#     display_name = data.get("display_name")
#     role = data.get("role", "normal_user")

#     if not all([email, first_name, last_name, display_name]):
#         return jsonify({"message": "All fields are required"}), 400

#     # Add user to the database
#     mongo.db.users.insert_one({
#         "email": email,
#         "first_name": first_name,
#         "last_name": last_name,
#         "display_name": display_name,
#         "role": role
#     })

#     # Generate a JWT token
#     access_token = create_access_token(identity={"email": email, "role": role})
#     return jsonify({"access_token": access_token, "message": "Onboarding completed"}), 201


# @auth_bp.route("/dashboard", methods=["GET"])
# @jwt_required()
# def dashboard():
#     """Access the dashboard based on user role."""
#     user = get_jwt_identity()
#     if user["role"] == "admin":
#         dashboard_items = ["Todo", "Chats", "Screens", "Meet", "Ideas", "Files", "Build", "Marketing"]
#     else:
#         dashboard_items = ["Todo", "Chats", "Screens", "Meet", "Ideas", "Files"]

#     return jsonify({"dashboard": dashboard_items}), 200
