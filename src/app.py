from flask import Flask, request, jsonify
from flask_restful import reqparse
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from celery import Celery

from repositories.MongoDB.TeachersMongoDBRepository import TeachersMongoDBRepository
from repositories.MongoDB.query_filters.TeacherMongoDBQueryFilter import TeacherMongoDBQueryFilter
from entities.Teacher import Teacher

from repositories.MongoDB.CoursesMongoDBRepository import CoursesMongoDBRepository 
from entities.Course import Course

celery = Celery('tasks', broker='amqp://rabbitmq:5672')

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongodb:27017/appDB"

app.secret_key = 'dRlo9fju-dRglo03e'
jwt = JWTManager(app)

teachersMongoDBRepository = TeachersMongoDBRepository(app)
coursesMongoDBRepository = CoursesMongoDBRepository(app)

teacherDTOParser = reqparse.RequestParser()
teacherDTOParser.add_argument(
    "username",
    type = str,
    required = True,
    help = "username is a required field"
)
teacherDTOParser.add_argument(
    "password",
    type = str,
    required = True,
    help = "password is a required field"
)

courseDTOParser = reqparse.RequestParser()
courseDTOParser.add_argument(
    "title",
    type = str,
    required = True,
    help = "title is a required field"
)

# TODO: Verify if a teacher already exists
# TODO: Validate the username(email)

@app.route('/user/signup', methods=['POST'])
def signup():
    teacherReqDTO = teacherDTOParser.parse_args()

    teacher = Teacher()
    teacher.username = teacherReqDTO["username"]
    teacher.password = teacherReqDTO["password"]
    
    teacherResDTO = teachersMongoDBRepository.create(teacher)

    celery.send_task("tasks.send_signup_email", [teacher.username])

    return jsonify({
        "uid": str(teacherResDTO.uid), 
        "username": teacherResDTO.username
    }), 200

@app.route('/user/login', methods=['POST'])
def login():
    teacherReqDTO = teacherDTOParser.parse_args()

    teacherMongoDBQueryFilter = TeacherMongoDBQueryFilter()
    teacherMongoDBQueryFilter.username = teacherReqDTO["username"]
    teacherMongoDBQueryFilter.password = teacherReqDTO["password"]

    teachers = teachersMongoDBRepository.query(teacherMongoDBQueryFilter)

    if teachers.count() == 0:
        return jsonify({"msg": "Bad username or password"}), 401

    accessTokenResDTO = {'access_token': create_access_token(identity=teacherReqDTO["username"])}

    return jsonify(accessTokenResDTO), 200

@app.route('/course', methods=["POST"])
@jwt_required
def insert_course():
    courseReqDTO = courseDTOParser.parse_args()
    
    course = Course()
    course.title = courseReqDTO["title"]
    
    courseResDTO = coursesMongoDBRepository.create(course)

    return jsonify({"uid": str(courseResDTO.uid), "title": courseResDTO.title}), 200