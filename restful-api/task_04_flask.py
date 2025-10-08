from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    username = list(users.keys())
    return jsonify(username)


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_username(username):
    user_username = users.get(username)
    if user_username:
        return jsonify(user_username)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data["username"]

    users[username] = {
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    return jsonify({
        "message": f"User '{username}' added successfully",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
