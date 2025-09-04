from flask import Blueprint, render_template, request, jsonify
from app.chatbot import get_chatbot_response
from app.journal import save_journal_entry
from app.resources import get_resources
from app.models import JournalEntry

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        user_input = request.form.get("message")
        response = get_chatbot_response(user_input)
        return jsonify({"response": response})
    return render_template("chatbot.html")

@main.route("/journal", methods=["GET", "POST"])
def journal():
    if request.method == "POST":
        user = "anonymous" # For hackathon: use auth for prod.
        content = request.form.get("entry")
        entry = save_journal_entry(user, content)
        return jsonify({"timestamp": entry.timestamp, "content": entry.content})
    return render_template("journal.html")

# --- CORRECTED ROUTE FOR JOURNAL HISTORY ---
@main.route('/journal/history')
def journal_history():
    user = "anonymous" # Make sure to get the correct user
    # This now correctly queries the database using your JournalEntry model
    entries = JournalEntry.query.filter_by(user=user).order_by(JournalEntry.content | JournalEntry.timestamp).all()
    return render_template('journal_history.html', entries=entries)

@main.route("/resources")
def resources():
    resources = get_resources()
    return render_template("resources.html", resources=resources)
