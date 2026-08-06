import os

import requests
from flask import Flask, Response, redirect, render_template, request, url_for


def create_app():
    app = Flask(__name__)
    app.config["BACKEND_URL"] = os.getenv("BACKEND_URL", "http://127.0.0.1:9000")

    @app.get("/")
    def home():
        return render_template("index.html", error=None, form={})

    @app.get("/api")
    @app.get("/data")
    def api_proxy():
        """Expose the backend JSON response through the browser-facing service."""
        try:
            response = requests.get(f'{app.config["BACKEND_URL"]}/api', timeout=10)
            return Response(
                response.content,
                status=response.status_code,
                content_type=response.headers.get("Content-Type", "application/json"),
            )
        except requests.RequestException as exc:
            return {"error": f"Could not contact the backend service: {exc}"}, 502

    @app.post("/submit")
    def submit():
        form_data = {
            "name": request.form.get("name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "course": request.form.get("course", "").strip(),
        }
        try:
            response = requests.post(
                f'{app.config["BACKEND_URL"]}/submit', json=form_data, timeout=10
            )
            if response.ok:
                return redirect(url_for("success"))
            try:
                error = response.json().get("error", "Submission failed")
            except ValueError:
                error = response.text or "Submission failed"
        except requests.RequestException as exc:
            error = f"Could not contact the backend service: {exc}"

        return render_template("index.html", error=error, form=form_data), 400

    @app.get("/success")
    def success():
        return render_template("success.html")

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8000, debug=True)
