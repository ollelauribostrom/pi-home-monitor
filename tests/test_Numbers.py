from src.Numbers import Numbers
from src.Log import Log
from tests.MockResponse import MockResponse

secret = "test_secret"
numbers = Numbers(secret)
log = Log()

def test_unauthorized_unauthorized():
  assert numbers.unauthorized("0701234567") == True

def test_authorize_success():
  response = numbers.authorize("0701234567", secret, MockResponse(), log)
  assert response.msg == 'Great, your number is now on the list of authorized numbers'

def test_unauthorized_authorized():
  assert numbers.unauthorized("0701234567") == False

def test_authorize_need_authorization():
  response = numbers.authorize("07012345678", "wrong_secret", MockResponse(), log)
  assert response.msg == 'Your number is not on the list of authorized numbers. Do you know the secret?'

def test_authorize_failed_authorization_attempt():
  response = numbers.authorize("07012345678", "wrong_secret", MockResponse(), log)
  assert response.msg == 'Wrong secret. You get one more chance. What is the secret?'

def test_authorize_failed_authorization():
  response = numbers.authorize("07012345678", "wrong_secret", MockResponse(), log)
  assert response.msg == 'Sorry, your number is now banned'

def test_authorize_banned():
  response = numbers.authorize("07012345678", "wrong_secret", MockResponse(), log)
  assert response.msg == None