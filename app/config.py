import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key")
    MONGO_URI = os.getenv("MONGO_URI", "your-mongodb-atlas-uri")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:5000/callback")
