import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()

def send_email(body, subject, to_email, from_email):
    password = os.getenv('APP_PASSWORD')
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        print("Connected to SMTP server.")
        server.login(from_email, password)
        print("Logged in to SMTP server.")
        server.send_message(msg)
        print("Email sent.")
        server.quit()
        print("Disconnected from SMTP server.")
        return "Success"
    except Exception as e:
        print(f"Failed to send email: {e}")
        return str(e)