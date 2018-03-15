def concerns_radio(msg):
  return 'radio' in msg.lower()

def includes_subscription(msg):
  message = msg.lower()
  words = ['subscription', 'notifying', 'movements', 'notifications']
  return word_checker(message, words)

def concerns_subscription(msg):
  if concerns_unsubscription(msg):
    return False
  else:
    message = msg.lower()
    words = ['start', 'subscribe', 'notify']
    return word_checker(message, words) and includes_subscription(message)
  
def concerns_unsubscription(msg):
  message = msg.lower()
  words = ['stop', 'end', 'unsubscribe']
  return word_checker(message, words) and includes_subscription(message)

def word_checker(message, words):
  for word in words:
    if word in message:
      return True
  else:
    return False