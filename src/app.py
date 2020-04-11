from flask import Flask

app = Flask(__name__)

@app.route('/course', methods=["POST"])
def insert_course():
    return 'Hello, World!'