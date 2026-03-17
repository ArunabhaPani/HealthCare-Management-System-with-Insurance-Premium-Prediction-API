import streamlit as st
import requests

API_URL = "http://prediction:8001/predict"

st.title("Insurance Premium Category Prediction")

st.markdown("""
This app predicts the insurance premium category based on user input. Please fill in the details below and click the "Predict" button to see the results.
""")

age = st.number_input("Age", min_value=1, max_value=120, value=30)
height = st.number_input("Height (in meters)", min_value=0.5, max_value=2.5, value=1.75)
weight = st.number_input("Weight (in kg)", min_value=1.0, value=70.0)
income_lpa = st.number_input("Annual Income (in LPA)", min_value=0.1, value=1.0)
smoker = st.selectbox("Smoker", options=[True, False])
city = st.text_input("City of Residence", value="New York")
occupation = st.selectbox("Occupation", options=['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])

if st.button("Predict"):
    input_data = {
        "age": age,
        "height": height,
        "weight": weight,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }
    
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance Premium Category: **{result['response']['predicted_category']}**")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the API. Please ensure the backend server is running at port 8001.")