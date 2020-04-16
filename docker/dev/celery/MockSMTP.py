import time

class MockSMTP():
  def __init__(self, address, port):
    pass

  def login(self, username, password):
    time.sleep(0.1)

  def sendmail(self, sender, receiver, message):
    time.sleep(0.6)

  def close(self):
    time.sleep(0.1)