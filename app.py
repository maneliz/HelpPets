from flask import Flask, request, make_response
from datetime import datetime
from flask_cors import CORS
import os
import requests

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

    # Дані для Google Sheets
    data = {
        "ip": request.remote_addr,
        "ua": request.headers.get("User-Agent")
    }

    # ВСТАВ СЮДИ СВІЙ URL Apps Script:
    url = "https://script.google.com/macros/s/AKfycbzuDHc7rD8BMCtkBXASdQV0CTGCUacQkyPIDVQOYMdJqUCoTrm8zL4MjawBzvF4tEWRWw/exec"

    try:
        requests.post(url, json=data)
    except Exception as e:
        print("Не вдалося записати в Google Sheets:", e)

    response = make_response("OK", 200)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
