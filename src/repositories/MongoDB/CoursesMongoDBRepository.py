from flask_pymongo import PyMongo

class CoursesMongoDBRepository():
  def __init__(self, application):
    self.mongo = PyMongo(application)

  def create(self, course):
    uid = self.mongo.db.courses.insert_one({"title": course.title}).inserted_id

    course.uid = uid

    return course