import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('PERPLEXITY_API_KEY')

def get_explanation(decision, stock, stock_data):
    """
    Generate an explanation for the AI's decision using Perplexity AI.
    """
    prompt = f"""
    Given the following stock data:
    {stock_data}

    The AI has decided to {decision} {stock}. Explain the reasoning behind this decision in terms of market trends, technical indicators, and any patterns that support the choice.
    """

    url = "https://api.perplexity.ai/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "You are a financial analyst providing insights on stock market trends. Limit response to 1 sentence."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Response Status Code: {response.status_code}")  # Debugging
        print(f"Response Text: {response.text}")  # Debugging

        if response.status_code == 200:
            response_json = response.json()
            return response_json["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code}, {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mock_data = [
        {"date": "2025-02-10", "open": 150.0, "close": 155.0, "high": 157.0, "low": 149.0, "volume": 1000000},
        {"date": "2025-02-11", "open": 156.0, "close": 158.0, "high": 160.0, "low": 154.0, "volume": 900000}
    ]
    print(get_explanation("BUY", "AAPL", mock_data))