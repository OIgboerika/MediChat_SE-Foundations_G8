from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy user data
users = {
    "john": {"password": "1234"},
    "jane": {"password": "5678"}
}

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username not in users:
        users[username] = {"password": password}
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "User already exists"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in users and users[username]["password"] == password:
        return jsonify({"status": "success", "username": username})
    return jsonify({"status": "error", "message": "Invalid credentials"})

if __name__ == "__main__":
    app.run()