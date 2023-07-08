import google.auth
from google.auth.transport.requests import Request

# Function to authenticate with Google Calendar API
def authenticate():
    creds, _ = google.auth.default()
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
    return creds