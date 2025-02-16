def generate_analysis(stock_symbol, decision, initial_value, final_value, last_price, news_summary):
    """Generate an analysis based on stock data, decision, and news."""
    
    analysis = f"Stock: {stock_symbol}\n"
    analysis += f"Initial predicted price: {initial_value}, Final predicted price: {final_value}, Last known price: {last_price}\n"
    analysis += f"Decision: {decision}\n"
    
    if decision == "BUY":
        analysis += "The model suggests a BUY as the stock is projected to trend upwards.\n"
    elif decision == "HOLD":
        analysis += "The model suggests HOLD since the last known price is higher than the final projection.\n"
    else:
        analysis += "The model suggests SELL as the trend is not strongly positive.\n"

    analysis += f"News Context: {news_summary}\n"

    return analysis