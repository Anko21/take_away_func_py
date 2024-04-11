from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import logging
import os

from dotenv import load_dotenv


# export TWILIO_ACCOUNT_SID=xxxxxxxxx
# export TWILIO_AUTH_TOKEN=xxxxxxxxx


client = Client()

def send_message(to, from_, message):
    try:
        sent_message = client.messages.create(
            to="+4407546854667",
            from_="+447401190288",
            body="Thank you! Your order was placed and will be delivered before 18:52" 
        )
    except TwilioRestException as e:
        logging.error(f'Oh no: {e}')
        return
    return sent_message.sid
