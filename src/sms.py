import os
from dotenv import load_dotenv
from os.path import join, dirname
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from src.Radio import Radio

load_dotenv(join(dirname(__file__), '../.env'))
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
radio = Radio()

def send_sms(toNumber, fromNumber, text):
  return client.messages.create(
    toNumber,
    body = text,
    from_ = fromNumber
  )

def sms_reply(data):
  incoming_msg = data['Body'].lower()
  resp = MessagingResponse()
  resp.message(create_reply(incoming_msg))
  return str(resp)

def create_reply(incoming_msg):
  if "radio" in incoming_msg:
    return radio.communicate(incoming_msg)
  else:
    return "What can I help you with?"