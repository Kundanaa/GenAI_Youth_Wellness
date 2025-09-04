# GenAI Youth Mental Wellness Web App

This project provides a confidential, AI-powered mental wellness platform for young people in India, leveraging Google Cloud's Generative AI (Gemini API) to offer empathetic support, journaling, and guidance.

## Features

- **Mental Wellness Chatbot:** Confidential, empathetic conversations with a generative AI, powered by Google Gemini.
- **Mood Journal:** Private journaling tool for emotional reflection and mood tracking.
- **Resource Finder:** Curated directory of mental health helplines, e-counseling portals, and self-help resources.

## Tech Stack

- **Backend:** Python (Flask), SQLAlchemy ORM
- **AI:** Google Gemini API for chatbot
- **Frontend:** HTML5, CSS3, JS (AJAX)
- **Database:** SQLite (for hackathon), MySQL recommended for production

## Setup and Usage

1. Set up your Google Gemini API Key and update `app/config.py`.

2. Install requirements:
```
pip install -r requirements.txt
```
3. Run app with:
```
python run.py
```
4. Access features at:
- **Home:** `/`
- **Chatbot:** `/chatbot`
- **Journal:** `/journal`
- **Resources:** `/resources`

## Notes

- User authentication is minimal for demo; build out as needed post-hackathon.
- All user data is stored securely and privately.
- Please ensure compliance with data privacy laws for any live deployment.

## Contributing

Fork the repo, make changes, and submit a pull request. Further enhancements—such as real-time mood analytics, peer group features, and therapist integration—are encouraged!

## License

MIT

## Acknowledgements

Thanks to Google Cloud, ACM Digital Library, Biz4Group, and Topflight Apps for sample architectures and ethical guidance