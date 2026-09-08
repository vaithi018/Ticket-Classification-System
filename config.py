import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration loaded from environment variables."""

    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

    # Database
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'tickets.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    # Ticket Classification
    CATEGORIES = [
        "Bug",
        "Feature Request",
        "Account/Billing",
        "Technical Support",
        "Security",
        "General Inquiry",
    ]

    PRIORITIES = ["Critical", "High", "Medium", "Low"]

    STATUSES = ["Open", "In Progress", "Resolved", "Closed"]

    TEAMS = [
        "Engineering",
        "Product",
        "Billing & Finance",
        "Customer Support",
        "Security Team",
        "General",
    ]
