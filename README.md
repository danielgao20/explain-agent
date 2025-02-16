# Analysis agent for stock decision system

## Backend Overview  
This project automates stock decision-making using **real-time stock data**, **news analysis**, and **AI-driven explanations**. The frontend was built with flutter.

## Features
- **Fetches stock data** from Alpaca API (stored in Firebase Firestore).  
- **Analyzes stock trends** using a CUDA-powered Decision Model.  
- **Generates AI-powered explanations** via Perplexity AI.  
- **Stores decisions & analysis** in Firestore for easy retrieval.  

## Installation
### **1. Clone the repository**  
```
git clone https://github.com/yourusername/explain-agent.git
cd explain-agent/backend
```

### **2. Set up python environment**  
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Configure Firebase**  
- Add your credentials.json inside the /config folder.
- Ensure Firestore is enabled in the Firebase Console.

## Usage
Run the main pipeline
```
python main.py
```

Run the API
```
python api/app.py
```
This will start a flask server to expose the decision results.
