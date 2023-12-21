from twilio.rest import Client
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_ACCOUNT_TOKEN')
phone_no = os.environ.get('PHONE')


def set_twilio_connection(account_sid, auth_token):
    client = Client(account_sid, auth_token)
    return client

def send_whatsapp_text(client,content):
    message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=content,
            to='whatsapp:+919065537902'
            )

    return message.sid

client = set_twilio_connection(account_sid, auth_token)
# def send_whatsapp_text(client,data):

# print(message.sid)