import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

from get_data import get_data

load_dotenv()

mens_winner, womens_winner = get_data()

subject = "NHD Contest Winner Announcement"
body = "Dear Adrian \n\nThe winner of the 2024 Nathan's Hot Dog Eating Contest is: \n\nMEN'S WINNER: " + \
        mens_winner + "\nWOMEN'S WINNER: " + womens_winner + "\n\nBest regards,\nSafak Simsek"
to_email = "safaksimsek5@berkeley.edu"
from_email = "safaksimsek05@gmail.com"


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