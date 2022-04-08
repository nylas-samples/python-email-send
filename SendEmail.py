# Load your env variables
from dotenv import load_dotenv
load_dotenv()

# Import your dependencies
import os
import sys
from nylas import APIClient

# Initialize your Nylas API client
nylas = APIClient(
    os.environ.get('CLIENT_ID'),
    os.environ.get('CLIENT_SECRET'),
    os.environ.get('ACCESS_TOKEN')
)

# Create a draft email
draft = nylas.drafts.create()
draft.subject = 'With Love, from Nylas'
draft.body = 'Well well well...'
draft.to = [{'name': 'Recipient name', 'email': os.environ.get('RECIPIENT_ADDRESS')}]

try:
# Send your email  
	message = draft.send()
	print("Message \"{}\" was sent with ID {}".format(message['subject'], message['id']))
except:
# Something went wrong  
	print("An {} error ocurred".format(sys.exc_info()[0]))
