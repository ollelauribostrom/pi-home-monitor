from src.EventEmitter import EventEmitter

emitter = EventEmitter()
event_counter = 0

def listener(ev):
  global event_counter
  if ev:
    event_counter += 1

def test_listen():
  emitter.listen('test', listener)

def test_emit():
  emitter.emit('test', 'data')

def test_event_recived():
  assert event_counter == 1