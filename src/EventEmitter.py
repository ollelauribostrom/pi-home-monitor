class EventEmitter:
  
  def __init__(self):
    self.listeners = []

  def listen(self, event, handler):
    if handler not in self.listeners:
      self.listeners.append({
        "event": event,
        "handler": handler
      })

  def emit(self, event, data):
    for handler in self.listeners:
      if handler['event'] == event:
        handler['handler'](data)