from flask import Flask
from app.extensions import jwt, mongo
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    jwt.init_app(app)
    mongo.init_app(app)

    # Register blueprints
    from app.auth.routes import auth_bp
    from app.onboarding.routes import onboarding_bp
    from app.dashboard.routes import dashboard_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(onboarding_bp, url_prefix="/onboarding")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")

    return app
