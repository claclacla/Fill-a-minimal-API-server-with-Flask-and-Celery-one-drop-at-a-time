from .randomString import randomString

def randomEmail():
  username = randomString()
  domain = randomString()

  return username + "@email.com" 