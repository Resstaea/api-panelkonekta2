import os, requests
from flask import Flask, jsonify

app = Flask(__name__)

API_URL = "http://51.77.216.195/crapi/konek/viewstats"
API_KEY = os.getenv("API_TOKEN")  # set di Railway Variables

@app.route("/")
def home():
    params = {"token": API_KEY, "records": 10}
    try:
        r = requests.get(API_URL, params=params, timeout=10)
        return jsonify(r.json())  # ini yg bikin tampil JSON rapi
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))