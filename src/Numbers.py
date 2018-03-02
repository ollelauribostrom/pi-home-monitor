class Numbers:

  def __init__(self, shared_secret):
    self.shared_secret = shared_secret
    self.authorized_numbers = []
    self.banned_numbers = []

  def unauthorized(self, number):
    return number not in self.authorized_numbers

  def authorize(self, number, message, response, log):
    if number in self.banned_numbers:
      pass
    elif message == self.shared_secret:
      self.authorized_numbers.append(number)
      response.message("Great, your number is now on the list of authorized numbers")
    elif log.latest(number) == log.Failed_Authorization:
      self.banned_numbers.append(number)
      response.message("Sorry, your number is now banned")
    elif log.latest(number) == log.Need_Authorization:
      log.add(log.Failed_Authorization, number)
      response.message("Wrong secret. You get one more chance. What is the secret?")
    else:
      log.add(log.Need_Authorization, number)
      response.message("Your number is not on the list of authorized numbers. Do you know the secret?")

    return response