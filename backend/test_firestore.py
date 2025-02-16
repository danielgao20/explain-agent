from config.firebase_setup import db

def test_stock_retrieval():
    """Test Firestore stock retrieval."""
    users_ref = db.collection("users")
    stock_docs = users_ref.stream()

    stock_symbols = [doc.id for doc in stock_docs]
    
    if not stock_symbols:
        print("⚠️ No stocks found in Firestore.")
    else:
        print(f"✅ Found {len(stock_symbols)} stocks: {stock_symbols}")

test_stock_retrieval()