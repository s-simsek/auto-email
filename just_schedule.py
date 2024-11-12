import datetime
import time

import schedule

from auto_email import send_email
from get_data import get_data

mens_winner, womens_winner = get_data()
subject = "NHD Contest Winner Announcement"
body = "Dear Adrian, \n\nThe winner of the 2024 Nathan's Hot Dog Eating Contest is: \n\nMEN'S WINNER: " + \
    mens_winner + "\nWOMEN'S WINNER: " + womens_winner + "\n\nBest regards,\nSafak Simsek"
to_email = "safaksimsek5@berkeley.edu"
from_email = "safaksimsek05@gmail.com"

def scheduled_email_job():
    # Send email    
    status = send_email(body, subject, to_email, from_email)
    if status == "Success":
        print({"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
               "subject": subject,
               "body": body,
               "to_email": to_email})
    else:
        print(f"Failed to send email: {status}")
        
if __name__ == '__main__':
    schedule.every(2).minutes.do(scheduled_email_job)
    while True:
        schedule.run_pending()
        time.sleep(1)   