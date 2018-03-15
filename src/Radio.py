import subprocess

class Radio:
  """CLI Radio Player dependent on npm module sverigesradio."""
  
  def __init__(self):
    self.__stream = None
    self.__playing = False
  
  def play(self):
    self.__stream = subprocess.Popen('sverigesradio')
    self.__playing = True

  def pause(self):
    self.__stream.terminate()
    self.__playing = False

  def is_playing(self):
    return self.__playing

  def communicate(self, number, message, response):
    if 'is' in message or 'status' in message:
      response.message('Radio is {}'.format('playing' if self.is_playing() else 'not playing'))
    elif 'start' in message or 'play' in message:
      self.play()
      response.message('Radio started')
    elif 'stop' in message or 'pause' in message:
      self.pause()
      response.message('Radio stopped')
    else:
      response.message('You can tell me to: "Start the radio", "Stop the radio" or ask me "Is the radio playing?"')
    return response