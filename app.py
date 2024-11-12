# app.py
import json
import os

from dotenv import load_dotenv
from filelock import FileLock
from flask import Flask, render_template

app = Flask(__name__)
load_dotenv()

# Define the path to the JSON file and lock file
EMAILS_FILE = 'emails.json'
LOCK_FILE = 'emails.lock'

@app.route('/')
def index():
    lock = FileLock(LOCK_FILE)
    with lock:
        if os.path.exists(EMAILS_FILE):
            with open(EMAILS_FILE, 'r') as f:
                emails = json.load(f)
        else:
            emails = []
    return render_template('index.html', emails=emails)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
