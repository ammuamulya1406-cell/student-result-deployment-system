from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/result/<student_id>')
def get_result(student_id):
    # Mock database response
    data = {"101": {"name": "Alice", "grade": "A"}, "102": {"name": "Bob", "grade": "B"}}
    return jsonify(data.get(student_id, {"error": "Student not found"}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
