from flask import jsonify

def BadRequest():
  return jsonify({"message": "Bad username or password"}), 400