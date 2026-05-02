# app/config.py
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_CONFIG = {
    "server": os.getenv("SMTP_SERVER"),
    "port": int(os.getenv("SMTP_PORT")),
    "email": os.getenv("SMTP_EMAIL"),
    "password": os.getenv("SMTP_PASSWORD")
}
GROQ_API_KEY = "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"

LOG_FOLDER_PATH = "data"

EMAIL_MAP = {
    "TEMPDB": "kamalakannan1011@gmail.com",
    "CAMP_CONTACT_HISTORY": "kamalakannan1011@gmail.com",
    "CAMP_INBOUND_FEEDBACK": "kamalakannan1011@gmail.com",
    "CAMP_OUTBOUND_FEEDBACK": "kamalakannan1011@gmail.com",
    "OTHER": "kamalakannan1011@gmail.com"
}

