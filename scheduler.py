import datetime
import os
import threading

from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

from auto_email import send_email
from get_data import get_data

load_dotenv()

# prepare email content
mens_winner, womens_winner = get_data()
subject = "NHD Contest Winner Announcement"
body = "Dear Adrian, \n\nThe winner of the 2024 Nathan's Hot Dog Eating Contest is: \n\nMEN'S WINNER: " + \
        mens_winner + "\nWOMEN'S WINNER: " + womens_winner + "\n\nBest regards,\nSafak Simsek"
to_email = "safaksimsek5@berkeley.edu"
from_email = "safaksimsek05@gmail.com"

def scheduled_email_job():
    status = send_email(body, subject, to_email, from_email)
    if status == "Success":
        print(f"Email sent successfully at {datetime.datetime.now()}")
    else:
        print(f"Failed to send email: {status}")

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled_email_job, 'interval', minutes=1)
    print("Scheduler started...")
    scheduler.start()