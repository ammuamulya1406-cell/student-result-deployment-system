from flask import Flask, jsonify
from flask_cors import CORS  # 1. Import CORS

app = Flask(__name__)
CORS(app)  # 2. Enable CORS for all routes

@app.route('/result/<student_id>')
def get_result(student_id):
    data = {"558": {"name": "Kushmitha", "grade": "A"}, "502": {"name": "Ammu", "grade": "B"},"549": {"name": "Akki", "grade": "A"}}
    return jsonify(data.get(student_id, {"error": "Student not found"}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
