from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "S-CIAX API Running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    return jsonify({"status": "ok", "input": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
