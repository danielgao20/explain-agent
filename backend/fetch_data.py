import json

def fetch_stock_data(symbol):
    # Simulated stock data
    sample_data = [
        {"date": "2025-02-10", "open": 150.0, "close": 155.0, "high": 157.0, "low": 149.0, "volume": 1000000},
        {"date": "2025-02-11", "open": 156.0, "close": 158.0, "high": 160.0, "low": 154.0, "volume": 900000},
        {"date": "2025-02-12", "open": 157.0, "close": 160.0, "high": 162.0, "low": 155.0, "volume": 950000},
        {"date": "2025-02-13", "open": 159.0, "close": 162.0, "high": 164.0, "low": 158.0, "volume": 1100000},
        {"date": "2025-02-14", "open": 161.0, "close": 165.0, "high": 166.0, "low": 160.0, "volume": 1050000},
    ]

    return json.dumps(sample_data)

if __name__ == "__main__":
    print(fetch_stock_data("AAPL"))