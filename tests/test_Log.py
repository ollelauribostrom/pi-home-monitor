from src.Log import Log

log = Log()

def test_exposed_properties():
  assert log.Failed_Authorization == 'failed_authorization'
  assert log.Need_Authorization == 'need_authorization'

def test_add():
  log.add(log.Need_Authorization, '0701234567')
  log.add(log.Failed_Authorization, '0701234567')

def test_latest():
  entry = log.latest('0701234567')
  assert entry == log.Failed_Authorization