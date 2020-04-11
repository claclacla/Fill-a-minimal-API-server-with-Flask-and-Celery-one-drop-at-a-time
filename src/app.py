from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongodb:27017/appDB"
mongo = PyMongo(app)

@app.route('/course', methods=["POST"])
def insert_course():
    courseRequestDTO = request.json
    mongo.db.courses.insert_one(courseRequestDTO)
    return courseRequestDTO["title"]