from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://mongodb:27017/appDB"
mongo = PyMongo(app)

app.secret_key = 'dRlo9fju-dRglo03e'
jwt = JWTManager(app)

users = {
    'teacher1': 'password1'
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username in users and users[username] == password:
        ret = {'access_token': create_access_token(identity=username)}
        return jsonify(ret), 200
        
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/course', methods=["POST"])
@jwt_required
def insert_course():
    courseRequestDTO = request.json
    mongo.db.courses.insert_one(courseRequestDTO)

    return jsonify({"title": courseRequestDTO["title"]}), 200