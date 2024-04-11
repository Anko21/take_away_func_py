from unittest.mock import Mock
from lib.send_sms import *

def test_calls_api_to_send_message_on_my_phone():
    requester_mock = Mock() # This name is just for readability
    # response_mock = Mock()


    # requester_mock.get.return_value = response_mock
    # response_mock.message.body.return_value = "- Thank you! Your order was placed and will be delivered before 18:52"

    message_sender = Message_sender(requester_mock)
    result = message_sender.send_message()

    assert result == "Sent from your Twilio trial account - Thank you! Your order was placed and will be delivered before 18:52"