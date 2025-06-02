from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return open("index.html", "r", encoding="utf-8").read()

@app.route("/log", methods=["POST"])
def log_click():
    with open("click_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - Натиснули кнопку\n")
    return "", 200

if __name__ == "__main__":
    app.run(port=5000)
