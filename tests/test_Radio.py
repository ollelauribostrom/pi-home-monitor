from src.Radio import Radio
from tests.MockResponse import MockResponse

radio = Radio()

def test_play():
  radio.play()
  assert radio.is_playing() == True

def test_pause():
  radio.pause()
  assert radio.is_playing() == False

def test_communicate_start():
  response = radio.communicate('0701234567', 'start radio', MockResponse())
  assert response.msg == 'Radio started'
  assert radio.is_playing() == True

def test_communicate_status_playing():
  response = radio.communicate('0701234567', 'is radio playing', MockResponse())
  assert response.msg == 'Radio is playing'

def test_communicate_stop():
  response = radio.communicate('0701234567', 'stop radio', MockResponse())
  assert response.msg == 'Radio stopped'
  assert radio.is_playing() == False

def test_communicate_status_playing_again():
  response = radio.communicate('0701234567', 'is radio playing', MockResponse())
  assert response.msg == 'Radio is not playing'

def test_communicate_other():
  response = radio.communicate('0701234567', 'adjandnui138', MockResponse())
  assert response.msg == 'You can tell me to: "Start the radio", "Stop the radio" or ask me "Is the radio playing?"'