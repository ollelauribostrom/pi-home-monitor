from src.message_rules import msg_concerns_radio, msg_concerns_camera

def test_concerns_radio():
  assert msg_concerns_radio("start radio") == True
  assert msg_concerns_radio("start RADIO something something") == True
  assert msg_concerns_radio("something something") == False

def test_concerns_camera():
  assert msg_concerns_camera("please notify me") == True
  assert msg_concerns_camera("stop notifying me") == True
  assert msg_concerns_camera("send me notifications") == True
  assert msg_concerns_camera("send me a picture of ..") == True
  assert msg_concerns_camera("send me a PIC of") == True
  assert msg_concerns_camera("send me a image of") == True
  assert msg_concerns_camera("something something") == False