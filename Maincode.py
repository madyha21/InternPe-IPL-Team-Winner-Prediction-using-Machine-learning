import streamlit as st
import pickle
import pandas as pd

# IPL Teams
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 
         'Rajasthan Royals', 'Delhi Capitals']

# Stadium Cities
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth', 
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley', 
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 
          'Mohali', 'Bengaluru']

# Load pre-trained model
pipe = pickle.load(open('pipe.pkl','rb'))

# Streamlit App
st.title('IPL Win Predictor')

# Create two columns for team selection
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))
    
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

# City selection
selected_city = st.selectbox('Select host city', sorted(cities))

# Match parameters
target = st.number_input('Target')

# Current match situation
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
    
with col4:
    overs = st.number_input('Overs completed')
    
with col5:
    wickets = st.number_input('Wickets out')

# Prediction button
if st.button('Predict Probability'):
    # Calculate match parameters
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    current_rr = score / overs if overs > 0 else 0
    required_rr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    # Create input dataframe for model
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'total_runs_x': [target],
        'cur_run_rate': [current_rr],
        'req_run_rate': [required_rr]
    })

    # Make prediction
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    
    # Display results
    st.header(batting_team + " - " + str(round(win * 100)) + "%")
    st.header(bowling_team + " - " + str(round(loss * 100)) + "%")
