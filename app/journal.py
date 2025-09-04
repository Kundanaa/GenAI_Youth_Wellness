from app.models import db, JournalEntry
from flask import request, jsonify
from datetime import datetime

def save_journal_entry(user, content):
    entry = JournalEntry(user=user, content=content, timestamp=datetime.now())
    db.session.add(entry)
    db.session.commit()
    return entry
