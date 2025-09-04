from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
