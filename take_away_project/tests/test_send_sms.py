from lib.send_sms import send_message
from unittest import mock
import os

def test_send_a_message():
    message = "Hi there"
    to="+4407546854667"
    from_="+447401190288"
    assert send_message(to, from_, message) is not None

@mock.patch('lib.send_sms.client.messages.create')
def test_send_a_message_mock(create_message_mock):
    message = "Hi there"
    expected_sid = 'SM87105da94bff44b999e4e6eb90d8eb6a'
    create_message_mock.return_value.sid = expected_sid

    to = "+4407546854667"
    from_ = "+447401190288"
    sid = send_message(to, from_, message)

    assert create_message_mock.called is True
    assert sid == expected_sid