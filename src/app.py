from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from repositories.MongoDB.TeachersMongoDBRepository import TeachersMongoDBRepository
from repositories.MongoDB.query_filters.TeacherMongoDBQueryFilter import TeacherMongoDBQueryFilter

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://mongodb:27017/appDB"
mongo = PyMongo(app)

app.secret_key = 'dRlo9fju-dRglo03e'
jwt = JWTManager(app)

teachersMongoDBRepository = TeachersMongoDBRepository(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    teacherMongoDBQueryFilter = TeacherMongoDBQueryFilter()
    teacherMongoDBQueryFilter.username = username
    teacherMongoDBQueryFilter.password = password

    teachers = teachersMongoDBRepository.query(teacherMongoDBQueryFilter)

    if teachers.count() == 0:
        return jsonify({"msg": "Bad username or password"}), 401

    response = {'access_token': create_access_token(identity=username)}

    return jsonify(response), 200

@app.route('/course', methods=["POST"])
@jwt_required
def insert_course():
    courseRequestDTO = request.json
    mongo.db.courses.insert_one(courseRequestDTO)

    return jsonify({"title": courseRequestDTO["title"]}), 200