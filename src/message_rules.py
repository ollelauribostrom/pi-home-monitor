def msg_concerns_radio(msg):
  return 'radio' in msg.lower()

def msg_concerns_camera(msg):
  message = msg.lower()
  words = ['notify', 'notifying', 'notifications', 'picture', 'pic', 'image']
  for word in words:
    if word in message:
      return True
  else:
    return False