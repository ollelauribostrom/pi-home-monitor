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

  def communicate(self, msg):
    if "is" in msg:
      return "Radio is {}".format("playing" if self.playing else "not playing")

    elif "start" in msg:
      self.start()
      return 'Radio started'

    elif "stop" in msg:
      self.stop()
      return 'Radio stopped'

    return 'Sure, I can help you with the radio: Start radio, Stop radio, Is radio playing?'