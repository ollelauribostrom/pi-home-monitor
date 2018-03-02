class Log:

  Failed_Authorization = 'failed_authorization'
  Need_Authorization = 'need_authorization'

  def __init__(self):
    self.entries = []

  def add(self, subject, number):
    self.entries.insert(0, {'subject': subject, 'number': number})

  def latest(self, number):
    for entry in self.entries:
      if entry['number'] == number:
        return entry['subject']