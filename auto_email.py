import os
import smtplib
import time
from email.message import EmailMessage

import schedule
from dotenv import load_dotenv

load_dotenv()

APP_PASSWORD = os.getenv('APP_PASSWORD')
def send_email(subject, body, to_email, from_email, password):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Use SMTP server for Gmail (modify if you use another service)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()
    print("Email sent!")

def job():
    # Define your email details
    subject = "Let's try to send an email"
    body = "Here's your update every 2 minutes."
    to_email = "safaksimsek5@berkeley.edu"
    from_email = "safaksimsek05@gmail.com"
    password = APP_PASSWORD # It's better to use environment variables or input this securely

    send_email(subject, body, to_email, from_email, password)

if __name__ == "__main__":
    # Schedule the job every 2 minutes
    schedule.every(2).minutes.do(job)

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)