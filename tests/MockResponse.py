class MockResponse:

  def __init__(self):
    self.msg = None
    
  def message(self, msg):
    self.msg = msg