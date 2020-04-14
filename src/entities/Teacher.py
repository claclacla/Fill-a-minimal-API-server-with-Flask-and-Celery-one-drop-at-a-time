class Teacher():
  def __init__(self):
    self.__username = None
    self.__password = None

  @property
  def username(self):
    return self.__username

  @username.setter
  def username(self, value):
    self.__username = value

  @property
  def password(self):
    return self.__password

  @password.setter
  def password(self, value):
    self.__password = value