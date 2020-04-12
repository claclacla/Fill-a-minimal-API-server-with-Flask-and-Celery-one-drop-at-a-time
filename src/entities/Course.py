class Course():
  def __init__(self):
    self.__uid = None
    self.__title = None

  @property
  def uid(self):
    return self.__uid

  @uid.setter
  def uid(self, value):
    self.__uid = value

  @property
  def title(self):
    return self.__title

  @title.setter
  def title(self, value):
    self.__title = value