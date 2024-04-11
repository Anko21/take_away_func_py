from twilio.rest import Client
import os

from dotenv import load_dotenv


class Message_sender:
    def __init__(self,requester):
        load_dotenv()
        self.requester = requester
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token  = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self):
        message = self.client.messages.create(
            to="+4407546854667",
            from_="+447401190288",
            body="Thank you! Your order was placed and will be delivered before 18:52" )
        return message.body