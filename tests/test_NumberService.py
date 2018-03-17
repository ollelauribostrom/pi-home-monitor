from src.NumberService import NumberService
from src.Log import Log
from tests.MockResponse import MockResponse

secret = 'test_secret'
log = Log()
numbers = NumberService({ 'shared_secret': secret }, log)

def test_is_authorized_fail():
  assert numbers.is_authorized('0701234567') == False

def test_authorize_success():
  response = numbers.authorize('0701234567', secret, MockResponse())
  assert response.msg == 'Great, your number is now on the list of authorized numbers'

def test_is_authorized_success():
  assert numbers.is_authorized('0701234567') == True

def test_authorize_need_authorization():
  response = numbers.authorize('07012345678', 'wrong_secret', MockResponse())
  assert response.msg == 'Hi! Your number is not on the list of authorized numbers. Do you know the secret?'

def test_authorize_failed_authorization_attempt():
  response = numbers.authorize('07012345678', 'wrong_secret', MockResponse())
  assert response.msg == 'Wrong secret. You get one more chance. What is the secret?'

def test_authorize_failed_authorization():
  response = numbers.authorize('07012345678', 'wrong_secret', MockResponse())
  assert response.msg == 'Sorry, your number is now banned'

def test_authorize_banned():
  response = numbers.authorize('07012345678', 'wrong_secret', MockResponse())
  assert response.msg == None

def test_is_banned_banned():
  assert numbers.is_banned('07012345678') == True

def test_is_banned_not_banned():
  assert numbers.is_banned('1234567') == False

def test_subscribe():
  numbers.subscribe('123')

def test_get_subscribers():
  assert len(numbers.get_subscribers()) == 1

def test_unsubscribe():
  numbers.unsubscribe('123')

def test_get_subscribers_empty():
  assert len(numbers.get_subscribers()) == 0

def test_token():
  token = numbers.generate_token()
  assert type(token) == str
  assert numbers.is_valid_token(token) == True

def test_invalid_token():
  assert numbers.is_valid_token('invalid') == False