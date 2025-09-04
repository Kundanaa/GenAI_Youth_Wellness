import logging
import requests
from flask import current_app
import os
import google.generativeai as genai

def get_chatbot_response(message: str) -> str:
    """
    Gets a response from the Google Gemini Pro model.

    Args:
        message: The user's message to send to the chatbot.

    Returns:
        The chatbot's text response or an error message.
    """
    try:
        # It's best practice to load the API key from an environment variable
        # rather than hardcoding it in your script.
        api_key = os.getenv("GOOGLE_API_KEY") or "AIzaSyBhIBM3FGjmFN0-JTt3GWE0boe5LgzrjgU"
        if not api_key:
            logging.error("GOOGLE_API_KEY environment variable not set.")
            return "Sorry, the chatbot is not configured correctly."

        genai.configure(api_key=api_key)

        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash-latest')

        # Send the message to the model and get the response
        response = model.generate_content(message)

        return response.text

    except Exception as e:
        # Catching a broad exception to handle various potential API errors
        logging.error(f"An error occurred with the Gemini API: {e}")
        return "Sorry, I am unable to respond right now."