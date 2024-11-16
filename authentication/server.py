from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Replace with a strong secret key
jwt = JWTManager(app)

# User data (replace with your actual user database)
users = {
    "testuser": {
        "password": "password123"  # Replace with a hashed password
    }
}

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", None)
    password = request.form.get("password", None)

    if username not in users or users[username]["password"] != password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"msg": "Protected route accessed successfully"})

@app.route("/resetpassword", methods=["POST"])
def test():
    return("<h1>Test</h1>")

if __name__ == "__main__":
    app.run(debug=True)