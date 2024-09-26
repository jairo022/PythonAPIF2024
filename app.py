from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)


@app.route("/", methods = ["GET"])

def home():
    return "Home"

client = MongoClient("mongodb+srv://jairomanuelfr:pxLgaQVG0hSwhPYI@cluster0.0dfey.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["L53FALL2024"]
users_collection = db["Users"]

print(users_collection)

@app.route("/users", methods = ["GET"])
def get_users():
    users = []
    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)