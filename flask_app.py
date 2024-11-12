import datetime
import os
import threading

from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from flask import Flask, render_template

from auto_email import send_email
from get_data import get_data

app = Flask(__name__)
load_dotenv()

# prepare email content
mens_winner, womens_winner = get_data()
subject = "NHD Contest Winner Announcement"
body = "Dear Adrian, \n\nThe winner of the 2024 Nathan's Hot Dog Eating Contest is: \n\nMEN'S WINNER: " + \
        mens_winner + "\nWOMEN'S WINNER: " + womens_winner + "\n\nBest regards,\nSafak Simsek"
to_email = "safaksimsek5@berkeley.edu"
from_email = "safaksimsek05@gmail.com"

# Storage for email details
emails_sent = []

# Lock to ensure thread safety
emails_sent_lock = threading.Lock()

def scheduled_email_job():
    # Send email
    status = send_email(body, subject, to_email, from_email)
    if status == "Success":
    # Acquire the lock before modifying the shared list
        with emails_sent_lock:
            emails_sent.append({
                "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "subject": subject,
                "body": body,
                "to_email": to_email
            })
    else:
        print(f"Failed to send email: {status}")


@app.route('/')
def index():
    with emails_sent_lock:
        emails_copy = list(emails_sent)  # Make a copy to release the lock early
    return render_template('index.html', emails=emails_copy)

if __name__ == '__main__':
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(scheduled_email_job, 'interval', minutes=1)
    scheduler.start()
    app.run(debug=True, use_reloader=False)  # use_reloader=False is important to not interfere with APScheduler
