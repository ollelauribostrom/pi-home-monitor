from uuid import uuid4

class NumberService:

  def __init__(self, config, log):
    self._shared_secret = config['shared_secret']
    self._log = log
    self._authorized_numbers = []
    self._banned_numbers = []
    self._subscribers = []
    self._tokens = []

  def is_authorized(self, number):
    return number in self._authorized_numbers

  def is_banned(self, number):
    return number in self._banned_numbers

  def subscribe(self, number):
    if number not in self._subscribers:
      self._subscribers.append(number)

  def unsubscribe(self, number):
    self._subscribers.remove(number)

  def get_subscribers(self):
    return self._subscribers

  def generate_token(self):
    token = str(uuid4())
    self._tokens.append(token)
    return token

  def is_valid_token(self, token):
    print(token)
    print(self._tokens)
    return token in self._tokens

  def authorize(self, number, message, response):
    if self.is_banned(number):
      pass
    elif message == self._shared_secret:
      self._authorized_numbers.append(number)
      response.message('Great, your number is now on the list of authorized numbers')
    elif self._log.latest(number) == self._log.Failed_Authorization:
      self._banned_numbers.append(number)
      response.message('Sorry, your number is now banned')
    elif self._log.latest(number) == self._log.Need_Authorization:
      self._log.add(self._log.Failed_Authorization, number)
      response.message('Wrong secret. You get one more chance. What is the secret?')
    else:
      self._log.add(self._log.Need_Authorization, number)
      response.message('Hi! Your number is not on the list of authorized numbers. Do you know the secret?')
    return response