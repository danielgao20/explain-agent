from flask import Flask, jsonify, request
from backend.temp import fetch_stock_data
from explanation import get_explanation
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask backend is running!"})

@app.route("/decision", methods=["GET"])
def get_decision():
    symbol = request.args.get("symbol", "AAPL")
    stock_data = fetch_stock_data(symbol)  # Fetch simulated stock data

    # Simulated decision-making logic (replace with actual C++ logic later)
    decision = "BUY" if symbol == "AAPL" else "HOLD"

    # Generate explanation using Perplexity AI
    explanation = get_explanation(decision, symbol, stock_data)

    return jsonify({"symbol": symbol, "decision": decision, "explanation": explanation})

if __name__ == "__main__":
    print("🚀 Running Flask backend on http://127.0.0.1:5001/")
    app.run(debug=True, host="0.0.0.0", port=5001)