from flask import Flask, request, make_response
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    response = make_response(content)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/log", methods=["POST", "OPTIONS"])
def log_click():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        return response

    with open("click_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Натиснули кнопку\n")

    response = make_response("OK", 200)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
