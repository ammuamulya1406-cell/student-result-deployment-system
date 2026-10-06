from flask import Flask, jsonify
from flask_cors import CORS  # 1. Import CORS

app = Flask(__name__)
CORS(app)  # 2. Enable CORS for all routes

@app.route('/result/<student_id>')
def get_result(student_id):
    data = {"101": {"name": "Alice", "grade": "A"}, "102": {"name": "Bob", "grade": "B"}}
    return jsonify(data.get(student_id, {"error": "Student not found"}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
