import subprocess

class Radio:
  """CLI Radio Player dependent on npm module sverigesradio."""
  
  def __init__(self):
    self.player = None
    self.playing = False
  
  def start(self):
    self.player = subprocess.Popen("sverigesradio")
    self.playing = True

  def stop(self):
    self.player.terminate()
    self.playing = False

  def communicate(self, number, message, response):
    if "is" in message:
      response.message("Radio is {}".format("playing" if self.playing else "not playing"))
    elif "start" in message:
      self.start()
      response.message('Radio started')
    elif "stop" in message:
      self.stop()
      response.message('Radio stopped')
    else:
      response.message('You can tell me to: "Start the radio", "Stop the radio" or ask me "Is the radio playing?"')

    return response