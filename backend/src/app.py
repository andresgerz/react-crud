from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost/reactcruddb"
mongo=PyMongo(app)

CORS(app)

db = mongo.db.users


@app.route("/user", methods=["POST"])
def createUser():
  print(request.json)
  id = db.insert({
    "name": request.json["name"],
    "surname": request.json["surname"],
    "email": request.json["email"],
    "age": request.json["age"],
    "password": request.json["password"]
  })

  return jsonify(str(ObjectId(id)))

@app.route("/users", methods=["GET"])
def getUsers():
  users = []

  for doc in db.find():
    users.append({
      "_id": str(ObjectId(doc["_id"])),
      "name": doc["name"],
      "surname": doc["surname"],
      "email": doc["email"],
      "age": doc["age"],
      "password": doc["password"]
    })
  return jsonify(users)

@app.route("/user/<id>", methods=["GET"])
def getUser(id):

  user = db.find_one({"_id": ObjectId(id)})
  return jsonify({
      "_id": str(ObjectId(user["_id"])),
      "name": user["name"],
      "surname": user["surname"],
      "email": user["email"],
      "age": user["age"],
      "password": user["password"]
  })

@app.route("/user/<id>", methods=["DELETE"])
def deleteUser(id):
  db.delete_one({
    "_id": ObjectId(id)
  })

  return jsonify({"message": "User deleted."})

@app.route("/user/<id>", methods=["PUT"])
def updateUser(id):
  db.update_one({"_id": ObjectId(id)}, {
    "$set": {
      "name": request.json["name"],
      "surname": request.json["surname"],
      "email": request.json["email"],
      "age": request.json["age"],
      "password": request.json["password"]
    }
  })
  return jsonify({"message": "User updated."})


if __name__ == "__main__":
  app.run(debug=True)