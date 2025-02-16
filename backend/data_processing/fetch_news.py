import requests
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('PERPLEXITY_API_KEY')

def fetch_stock_news(stock_symbol):
    """Fetch financial news related to the stock symbol."""
    
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    prompt = f"Provide a financial news summary for {stock_symbol} on {date}."

    url = "https://api.perplexity.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "You are a financial analyst providing insights on stock market trends."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"]
    else:
        return f"Error fetching news: {response.status_code}, {response.text}"
