import streamlit as st

# Page settings
st.set_page_config(page_title="Aviation Risk Predictor", page_icon="✈️")

# Title
st.title("✈️ Aviation Risk Predictor")

# Text
st.write("Enter flight details:")

# Inputs
weather = st.selectbox(
    "Weather",
    ["Good (0)", "Bad (1)"]
)

delay = st.selectbox(
    "Flight Delay",
    ["No (0)", "Yes (1)"]
)

maintenance = st.selectbox(
    "Maintenance Issue",
    ["No (0)", "Yes (1)"]
)

experience = st.number_input(
    "Pilot Experience (years)",
    min_value=1,
    value=1,
    step=1
)

age = st.number_input(
    "Aircraft Age (years)",
    min_value=1,
    value=1,
    step=1
)

# Predict Button
if st.button("Predict Risk"):

    risk_score = 0

    # Convert values
    weather_val = 1 if weather == "Bad (1)" else 0
    delay_val = 1 if delay == "Yes (1)" else 0
    maintenance_val = 1 if maintenance == "Yes (1)" else 0

    # Logic
    if weather_val == 1:
        risk_score += 2

    if delay_val == 1:
        risk_score += 1

    if maintenance_val == 1:
        risk_score += 3

    if experience < 3:
        risk_score += 2
    elif experience < 7:
        risk_score += 1

    if age > 20:
        risk_score += 2
    elif age > 10:
        risk_score += 1

    # Result
    st.subheader("Result")

    if risk_score <= 2:
        st.success("Low Risk ✅")
    elif risk_score <= 5:
        st.warning("Medium Risk ⚠️")
    else:
        st.error("High Risk 🚨")
