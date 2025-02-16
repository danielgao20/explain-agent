from config.firebase_setup import db

def fetch_stock_data(stock_symbol):
    """Fetch stock data from Firestore."""
    stock_ref = db.collection("users").document(stock_symbol)  # Fetch from users collection
    stock_data = stock_ref.get()

    if stock_data.exists:
        data = stock_data.to_dict()
        print(f"✅ Retrieved data for {stock_symbol}: {data}")  # Debug print

        # Extract the relevant values
        best_path = data.get("bestPath", [])
        last_price = data.get("lastPrice", None)

        if not best_path or last_price is None:
            print(f"⚠️ Missing data for {stock_symbol}. Skipping.")
            return None, None, None

        # Get first and last values from bestPath
        initial_value = best_path[0]
        final_value = best_path[-1]

        return initial_value, final_value, last_price
    else:
        print(f"❌ Stock {stock_symbol} not found in Firestore.")
        return None, None, None