def msg_concerns_radio(msg):
  return 'radio' in msg.lower()

def msg_concerns_subscription(msg):
  message = msg.lower()
  words = ['start', 'subscribe', 'notify']
  return word_checker(message, words)
  
def msg_concerns_unsubscription(msg):
  message = msg.lower()
  words = ['stop', 'unsubscribe']
  return word_checker(message, words)

def word_checker(message, words):
  for word in words:
    if word in message:
      return True
  else:
    return False