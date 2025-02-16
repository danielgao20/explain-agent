from config.firebase_setup import db

def store_analysis(stock_symbol, decision, analysis):
    """Store stock decision and analysis in Firestore."""
    analysis_ref = db.collection("analysis").document(stock_symbol)  # Reference Firestore collection
    analysis_ref.set({
        "decision": decision,
        "analysis": analysis
    })
    print(f"✅ Stored analysis for {stock_symbol}.")