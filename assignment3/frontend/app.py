from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

backend_url = "http://127.0.0.1:9000"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]

    form_data = {
        "name": name,
        "email": email,
        "course": course
    }

    try:
        response = requests.post(backend_url + "/submit", json=form_data)

        if response.json().get("message") == "Data submitted successfully":
            return redirect("/success")
        else:
            error = response.json().get("error")
            return render_template("index.html", error=error)
    except Exception as error:
        return render_template("index.html", error=error)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
