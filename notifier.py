# app/notifier.py

import smtplib
from email.mime.text import MIMEText
from config import SMTP_CONFIG

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_CONFIG["email"]
    msg["To"] = to_email

    with smtplib.SMTP(SMTP_CONFIG["server"], SMTP_CONFIG["port"]) as server:
        server.starttls()
        server.login(SMTP_CONFIG["email"], SMTP_CONFIG["password"])
        server.send_message(msg)