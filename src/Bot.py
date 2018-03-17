import threading
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import src.utils.message_rules as rules
import src.utils.url_utils as url

class Bot():

  def __init__(self, config, numbers, radio):
    self._config = config
    self._numbers = numbers
    self._radio = radio
    self._client = Client(config['account_sid'], config['auth_token'])
  
  def reply(self, data):
    number = data['From']
    message = data['Body']
    return str(self._make_response(number, message))

  def _make_response(self, number, message):
    response = MessagingResponse()
    if not self._numbers.is_authorized(number):
      return self._numbers.authorize(number, message, response)
    elif rules.concerns_radio(message):
      return self._radio.communicate(number, message.lower(), response)
    elif rules.concerns_subscription(message):
      self._numbers.subscribe(number)
      response.message('Cool, you are now reciving notifications from the monitor')
      return response
    elif rules.concerns_unsubscription(message):
      self._numbers.unsubscribe(number)
      response.message('Ok, you will no longer recive notifications from the monitor')
      return response
    else:
      reply = 'Sorry, i did not understand "{}". What can I help you with?'.format(message)
      response.message(reply)
      return response

  def send(self, to, text):
    return self._client.messages.create(
      to,
      body = text,
      from_ = self._config['from']
    )

  def motion_handler(self, video):
    token = self._numbers.generate_token()
    base_url = url.format(self._config['base_url'])
    message = 'Movements @ {}/video/{}?token={}'.format(base_url, video, token)
    for number in self._numbers.get_subscribers():
      self.send(number, message)
