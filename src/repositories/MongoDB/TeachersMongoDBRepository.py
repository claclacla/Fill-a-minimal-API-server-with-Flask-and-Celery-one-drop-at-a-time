from flask_pymongo import PyMongo

class TeachersMongoDBRepository():
  def __init__(self, application):
    self.mongo = PyMongo(application)

  def query(self, teacherMongoDBQueryFilter):
    teachers = self.mongo.db.teachers.find(teacherMongoDBQueryFilter.getFilter())

    return teachers