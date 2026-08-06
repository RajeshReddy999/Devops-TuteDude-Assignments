import json
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"


def create_app(collection=None):
    load_dotenv(BASE_DIR / ".env")
    app = Flask(__name__)

    if collection is None:
        mongo_uri = os.getenv("MONGO_URI")
        if not mongo_uri:
            raise RuntimeError("MONGO_URI is not configured. Copy .env.example to .env and add your Atlas URI.")
        # Defer network discovery until a database operation so /api remains
        # available even when Atlas or DNS is temporarily unreachable.
        client = MongoClient(
            mongo_uri,
            server_api=ServerApi("1"),
            serverSelectionTimeoutMS=5000,
            connect=False,
        )
        collection = client[os.getenv("MONGO_DB", "assignment3")][os.getenv("MONGO_COLLECTION", "submissions")]

    app.config["COLLECTION"] = collection

    @app.get("/api")
    def api():
        """Read the backend JSON file and return its list as JSON."""
        try:
            with DATA_FILE.open(encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("The backend data file must contain a JSON list.")
            return jsonify(data)
        except (OSError, json.JSONDecodeError, ValueError) as error:
            return jsonify({"error": f"Unable to read backend data: {error}"}), 500

    @app.post("/submit")
    def submit():
        payload = request.get_json(silent=True) or {}
        required = ("name", "email", "course")
        missing = [field for field in required if not str(payload.get(field, "")).strip()]
        if missing:
            return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

        document = {field: str(payload[field]).strip() for field in required}
        try:
            result = app.config["COLLECTION"].insert_one(document)
            return jsonify({"message": "Data submitted successfully", "id": str(result.inserted_id)}), 201
        except Exception as error:
            app.logger.exception("MongoDB insertion failed")
            return jsonify({"error": f"Database submission failed: {error}"}), 500

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=9000, debug=True, use_reloader=False)
