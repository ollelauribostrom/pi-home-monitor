class EventEmitter:
  
  def __init__(self):
    self._listeners = []

  def listen(self, event, handler):
    if handler not in self._listeners:
      self._listeners.append({
        'event': event,
        'handler': handler
      })

  def emit(self, event, data):
    for handler in self._listeners:
      if handler['event'] == event:
        handler['handler'](data)