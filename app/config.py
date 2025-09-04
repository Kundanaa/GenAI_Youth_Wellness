import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key"
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or "AIzaSyBhIBM3FGjmFN0-JTt3GWE0boe5LgzrjgU"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///genai_youth_wellness.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False