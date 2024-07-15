from nylas import Client
from dotenv import load_dotenv
import os

# Load our .env file
load_dotenv()

# Initialize Nylas client
nylas = Client(
    api_key = os.environ.get("NYLAS_API_KEY"),
    api_uri = os.environ.get('NYLAS_API_URI')
)

body = {
            "subject" : "With Love, from Nylas V3", 
            "body":"Well well well...",
            "to" : [{"email": os.environ.get("RECIPIENT_EMAIL")}]
        }

try:
    message = nylas.messages.send(os.environ.get("NYLAS_GRANT_ID"), request_body = body).data
    print(f"Message \"{message.subject}\" was sent with ID {message.id}")
except Exception as e:
	print(f"An error ocurred: {e}")
