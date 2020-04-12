from flask import Flask, request, jsonify
from flask_restful import reqparse
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from repositories.MongoDB.TeachersMongoDBRepository import TeachersMongoDBRepository
from repositories.MongoDB.query_filters.TeacherMongoDBQueryFilter import TeacherMongoDBQueryFilter

from repositories.MongoDB.CoursesMongoDBRepository import CoursesMongoDBRepository 
from entities.Course import Course

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

@app.route('/login', methods=['POST'])
def login():
    teacherDTO = teacherDTOParser.parse_args()

    teacherMongoDBQueryFilter = TeacherMongoDBQueryFilter()
    teacherMongoDBQueryFilter.username = teacherDTO["username"]
    teacherMongoDBQueryFilter.password = teacherDTO["password"]

    teachers = teachersMongoDBRepository.query(teacherMongoDBQueryFilter)

    if teachers.count() == 0:
        return jsonify({"msg": "Bad username or password"}), 401

    response = {'access_token': create_access_token(identity=teacherDTO["username"])}

    return jsonify(response), 200

@app.route('/course', methods=["POST"])
@jwt_required
def insert_course():
    title = request.json.get("title", None)
    
    course = Course()
    course.title = title
    
    course = coursesMongoDBRepository.create(course)

    return jsonify({"uid": str(course.uid), "title": course.title}), 200