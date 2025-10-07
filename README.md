# InternPe-IPL-Team-Winner-Prediction-using-Machine-learning
A real-time IPL (Indian Premier League) win probability predictor built with Streamlit that calculates winning chances for batting teams during live matches based on current match situation.
🎯 Features

· Real-time Predictions: Calculate win probability during live matches
· Team Selection: Choose from all IPL teams
· Match Context: Consider venue, target, current score, overs, and wickets
· Interactive UI: User-friendly Streamlit web interface
· Probability Display: Show winning percentages for both teams

🛠️ Technology Stack

· Frontend: Streamlit
· Backend: Python
· Machine Learning: Pre-trained model (pipe.pkl)
· Data Handling: Pandas
· Model Persistence: Pickle

📁 Project Structure

```
IPL-Win-Predictor/
│
├── Proj3.py                 # Main Streamlit application
├── pipe.pkl                 # Pre-trained machine learning model
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
└── assets/
    └── images/             # Screenshots and demo images
```

📦 Installation & Setup

1. Create requirements.txt

```txt
streamlit>=1.28.0
pandas>=1.5.0
scikit-learn>=1.2.0
numpy>=1.21.0
pickle-mixin>=1.0.0
```

2. Installation Steps

```bash
# Clone repository
git clone <your-repo-url>
cd IPL-Win-Predictor

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run Proj3.py
```

🚀 Usage

1. Select Teams: Choose batting and bowling teams from dropdown
2. Set Match Context:
   · Select host city
   · Enter target runs
   · Input current score, overs completed, and wickets fallen
3. Get Prediction: Click "Predict Probability" button
4. View Results: See winning percentages for both teams

🔧 Key Functionality

· Real-time Calculations: Dynamically computes runs required, balls remaining, and required run rate
· Probability Prediction: Uses pre-trained ML model to predict win/loss probabilities
· Interactive Interface: User-friendly web interface built with Streamlit

🤖 Machine Learning Features

The model considers:

· Team Strengths: Batting and bowling team capabilities
· Match Situation: Runs needed, balls remaining, wickets in hand
· Venue Factors: Home advantage and pitch conditions
· Run Rates: Current and required run rates. 


📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Madiha Manzoor

