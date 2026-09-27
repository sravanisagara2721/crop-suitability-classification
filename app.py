import joblib
import pandas as pd
import streamlit as st


# Load model and training data
model = joblib.load("crop_recommendation_model.pkl")
data = pd.read_csv("Crop_recommendation.csv")


# Page configuration
st.set_page_config(
    page_title="Crop Suitability Predictor",
    page_icon="🌱",
    layout="centered"
)


st.title("🌱 Crop Suitability Predictor")
st.write(
    "Enter the soil and weather conditions to predict a suitable crop."
)


# Get feature ranges from the dataset
feature_columns = [
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall"
]


# Input section
st.subheader("Soil and Weather Details")

nitrogen = st.number_input(
    "Nitrogen (N)",
    min_value=float(data["N"].min()),
    max_value=float(data["N"].max()),
    value=float(data["N"].mean())
)

phosphorus = st.number_input(
    "Phosphorus (P)",
    min_value=float(data["P"].min()),
    max_value=float(data["P"].max()),
    value=float(data["P"].mean())
)

potassium = st.number_input(
    "Potassium (K)",
    min_value=float(data["K"].min()),
    max_value=float(data["K"].max()),
    value=float(data["K"].mean())
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=float(data["temperature"].min()),
    max_value=float(data["temperature"].max()),
    value=float(data["temperature"].mean())
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=float(data["humidity"].min()),
    max_value=float(data["humidity"].max()),
    value=float(data["humidity"].mean())
)

ph = st.number_input(
    "Soil pH",
    min_value=float(data["ph"].min()),
    max_value=float(data["ph"].max()),
    value=float(data["ph"].mean())
)

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=float(data["rainfall"].min()),
    max_value=float(data["rainfall"].max()),
    value=float(data["rainfall"].mean())
)


# Prediction
if st.button("Predict Crop"):

    input_data = pd.DataFrame(
        [[
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        ]],
        columns=feature_columns
    )

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]
    probability = probabilities.max()

    st.success(f"Recommended Crop: {prediction}")

    st.info(
        f"Model probability for this prediction: "
        f"{probability * 100:.2f}%"
    )