from data_processing.fetch_stock_data import fetch_stock_data
from data_processing.decision_logic import make_decision
from data_processing.fetch_news import fetch_stock_news
from data_processing.generate_analysis import generate_analysis
from data_processing.store_analysis import store_analysis
from config.firebase_setup import db

def get_all_stock_symbols():
    """Retrieve all stock symbols from Firestore (document IDs in 'users' collection)."""
    users_ref = db.collection("users")
    stock_docs = users_ref.stream()  # Fetch all documents in "users" collection

    stock_symbols = [doc.id for doc in stock_docs]  # Extract document IDs (stock symbols)

    if not stock_symbols:
        print("⚠️ No stocks found in Firestore.")
    else:
        print(f"✅ Found {len(stock_symbols)} stocks in Firestore.")

    return stock_symbols

def main():
    """Run the full pipeline for all stocks in Firestore."""
    stock_symbols = get_all_stock_symbols()
    
    if not stock_symbols:
        print("No stocks found in Firestore.")
        return

    print(f"Processing {len(stock_symbols)} stocks...")

    for stock_symbol in stock_symbols:
        # Fetch stock data
        initial_value, final_value, last_price = fetch_stock_data(stock_symbol)

        if initial_value is None or final_value is None or last_price is None:
            print(f"Skipping {stock_symbol} due to missing data.")
            continue

        # Determine the decision
        decision = make_decision(initial_value, final_value, last_price)

        # Fetch stock news
        news_summary = fetch_stock_news(stock_symbol)

        # Generate analysis
        analysis = generate_analysis(stock_symbol, decision, initial_value, final_value, last_price, news_summary)

        # Store analysis in Firestore
        store_analysis(stock_symbol, decision, analysis)

        print(f"Completed processing for {stock_symbol}.")

if __name__ == "__main__":
    main()