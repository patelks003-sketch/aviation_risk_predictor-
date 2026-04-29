import streamlit as st

# Page setup
st.set_page_config(page_title="Aviation Risk Predictor")

# Title
st.title("✈ Aviation Risk Predictor")

# Description
st.write("This app predicts aviation risk level")

# Inputs
altitude = st.number_input("Enter altitude (feet)", min_value=0)
weather = st.selectbox("Weather condition", ["Clear", "Cloudy", "Storm"])

# Prediction
if st.button("Predict Risk"):
    if altitude > 30000 and weather == "Storm":
        st.error("High Risk ✈⚠")
    elif altitude > 20000:
        st.warning("Medium Risk ⚠")
    else:
        st.success("Low Risk ✅")
