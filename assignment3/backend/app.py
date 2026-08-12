from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import json
import os

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
database = client["assignment3"]
collection = database["students"]


@app.route("/api/local")
def api():
    file = open("data.json", "r")
    data = json.load(file)
    file.close()
    return jsonify(data)


@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = request.get_json()
        collection.insert_one(data)
        return jsonify({"message": "Data submitted successfully"})
    except Exception as error:
        return jsonify({"error": str(error)})


if __name__ == "__main__":
    app.run(port=9000, debug=True)
