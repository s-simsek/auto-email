# scheduler.py
import datetime
import json
import os

from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv
from filelock import FileLock

from auto_email import send_email
from get_data import get_data

load_dotenv()

# Prepare email content
mens_winner, womens_winner = get_data()
subject = "NHD Contest Winner Announcement"
body = (
    "Dear Adrian, \n\nThe winner of the 2024 Nathan's Hot Dog Eating Contest is: \n\nMEN'S WINNER: "
    + mens_winner
    + "\nWOMEN'S WINNER: "
    + womens_winner
    + "\n\nBest regards,\nSafak Simsek"
)
to_email = "adrian@lechterventures.com"
from_email = "safaksimsek05@gmail.com"

# Define the path to the JSON file and lock file
EMAILS_FILE = 'emails.json'
LOCK_FILE = 'emails.lock'

def scheduled_email_job():
    status = send_email(body, subject, to_email, from_email)
    if status == "Success":
        print(f"Email sent successfully at {datetime.datetime.now()}")
        # Save email record to the JSON file
        email_record = {
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "subject": subject,
            "body": body,
            "to_email": to_email
        }
        # Use file lock to ensure safe write operation
        lock = FileLock(LOCK_FILE)
        with lock:
            if os.path.exists(EMAILS_FILE):
                with open(EMAILS_FILE, 'r') as f:
                    emails = json.load(f)
            else:
                emails = []
            emails.append(email_record)
            with open(EMAILS_FILE, 'w') as f:
                json.dump(emails, f)
    else:
        print(f"Failed to send email: {status}")

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled_email_job, 'interval', hours=24)
    print("Scheduler started...")
    scheduler.start()
