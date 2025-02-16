import requests
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('PERPLEXITY_API_KEY')

def test_fetch_news():
    """Test Perplexity API for fetching stock news and print the output in plain text."""
    stock_symbol = "AAPL"  # Change this to test other stocks
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
    Summarize the most important financial news for {stock_symbol} on {date}. 
    Provide the key takeaways in a plain-text format without any emojis, special characters, or unnecessary formatting.
    End with a source link if available.
    """

    url = "https://api.perplexity.ai/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "You are a financial analyst providing clear, concise, and confident stock market insights."},
            {"role": "user", "content": prompt}
        ]
    }

    print("Sending request to Perplexity API...")

    try:
        response = requests.post(url, headers=headers, json=data)

        print("API Response Status:", response.status_code)

        if response.status_code == 200:
            response_json = response.json()
            news_summary = response_json["choices"][0]["message"]["content"]
            
            # Ensure plain text format
            news_summary = news_summary.replace("*", "").replace("_", "").replace("•", "").strip()
            
            print("\nGenerated News Summary:")
            print(news_summary)

        else:
            print(f"Error fetching news: {response.status_code}, {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Run the test
test_fetch_news()
