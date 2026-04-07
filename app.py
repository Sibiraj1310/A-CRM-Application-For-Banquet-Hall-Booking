from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "CRM Banquet Hall Backend Running"

@app.route('/book', methods=['POST'])
def book():
    data = request.json
    return jsonify({"message": "Booking Saved", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
