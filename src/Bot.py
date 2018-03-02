from src.message_rules import msg_concerns_radio, msg_concerns_camera
from twilio.twiml.messaging_response import MessagingResponse
from src.Radio import Radio
from src.Camera import Camera
from src.Log import Log
from src.Numbers import Numbers

class Bot:

  def __init__(self, shared_secret):
    self.radio = Radio()
    self.camera = Camera()
    self.log = Log()
    self.numbers = Numbers(shared_secret)
  
  def reply(self, data):
    number = data['From']
    message = data['Body']
    return str(self.make_response(number, message))

  def make_response(self, number, message, response):
    response = MessagingResponse()
    if self.numbers.unauthorized(number):
      return self.numbers.authorize(number, message, response, self.log)
    elif msg_concerns_radio(message):
      return self.radio.communicate(number, message.lower(), response)
    elif msg_concerns_camera(message):
      return self.camera.communicate(number, message.lower(), response)
    else:
      response.message("What can I help you with?")
      return response

