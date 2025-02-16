def make_decision(initial_value, final_value, last_price):
    """Determine buy/sell/hold decision based on stock price movement."""
    
    if final_value < last_price:
        decision = "HOLD"
    elif final_value > initial_value:
        decision = "BUY"
    else:
        decision = "SELL"

    return decision