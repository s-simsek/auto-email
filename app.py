# app.py
import os

from dotenv import load_dotenv
from flask import Flask, render_template

from models import EmailRecord, Session  # Import from your models module

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    session = Session()
    emails = session.query(EmailRecord).order_by(EmailRecord.time_sent.desc()).all()
    session.close()
    return render_template('index.html', emails=emails)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
