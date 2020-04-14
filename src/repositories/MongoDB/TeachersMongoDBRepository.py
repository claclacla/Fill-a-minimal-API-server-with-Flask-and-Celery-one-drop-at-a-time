from flask_pymongo import PyMongo

class TeachersMongoDBRepository():
  def __init__(self, application):
    self.mongo = PyMongo(application)

  def create(self, teacher):
    uid = self.mongo.db.teachers.insert_one({
      "username": teacher.username,
      "password": teacher.password
    }).inserted_id

    teacher.uid = uid

    return teacher

  def query(self, teacherMongoDBQueryFilter):
    teachers = self.mongo.db.teachers.find(teacherMongoDBQueryFilter.getFilter())

    return teachers