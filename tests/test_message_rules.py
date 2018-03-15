from src import message_rules as rules

def test_concerns_radio():
  assert rules.concerns_radio('start radio') == True
  assert rules.concerns_radio('start RADIO something something') == True
  assert rules.concerns_radio('something something') == False

def test_includes_subscription():
  assert rules.includes_subscription('start Subscription') == True
  assert rules.includes_subscription('start notifying me') == True
  assert rules.includes_subscription('track movements') == True
  assert rules.includes_subscription('something something') == False

def test_concerns_subscription():
  assert rules.concerns_subscription('start notifying me') == True
  assert rules.concerns_subscription('subscribe to notifications') == True
  assert rules.concerns_subscription('notify me on movements') == True
  assert rules.concerns_subscription('stop notifying me') == False

def test_concerns_unsubscription():
  assert rules.concerns_unsubscription('stop notifying me') == True
  assert rules.concerns_unsubscription('end subscription') == True
  assert rules.concerns_unsubscription('unsubscribe from notifications') == True
  assert rules.concerns_unsubscription('start notifying me') == False

