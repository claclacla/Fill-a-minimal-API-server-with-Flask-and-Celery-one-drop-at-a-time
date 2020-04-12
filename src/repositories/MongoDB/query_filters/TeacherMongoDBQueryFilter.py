class TeacherMongoDBQueryFilter():
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

  def getFilter(self):
    filter = {}

    if self.__username is not None:
      filter["username"] = self.__username

    if self.__password is not None:
      filter["password"] = self.__password

    return filter