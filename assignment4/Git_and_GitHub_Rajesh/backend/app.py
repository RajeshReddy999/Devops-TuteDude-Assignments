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
todo_collection = database["todo_items"]


@app.route("/")
def hello_world():
    return 'Hello from assignment 4'

@app.route("/api")
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


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    try:
        item_name = request.form["itemName"]
        item_description = request.form["itemDescription"]

        todo_item = {
            "itemName": item_name,
            "itemDescription": item_description
        }

        todo_collection.insert_one(todo_item)
        return jsonify({"message": "To-Do item saved successfully"})
    except Exception as error:
        return jsonify({"error": str(error)})


if __name__ == "__main__":
    app.run(port=9000, debug=True)
