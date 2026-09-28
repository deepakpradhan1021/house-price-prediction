import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model.pkl")

st.title("🏠 House Price Predictor")
st.write("Enter the house details to estimate its price.")

# Features
columns = [
    "OverallQual",
    "GrLivArea",
    "GarageCars",
    "TotalBsmtSF",
    "YearBuilt",
    "FullBath"
]

qual = st.slider("Overall Quality (1-10)", 1, 10, 5)

area = st.number_input(
    "Living Area (sq ft)",
    min_value=500,
    max_value=6000,
    value=1500
)

garage = st.slider("Garage Capacity (cars)", 0, 4, 2)

bsmt = st.number_input(
    "Basement Area (sq ft)",
    min_value=0,
    max_value=4000,
    value=800
)

year = st.number_input(
    "Year Built",
    min_value=1870,
    max_value=2010,
    value=1990
)

bath = st.slider("Full Bathrooms", 0, 4, 2)

# Prediction
if st.button("Predict Price"):

    X = pd.DataFrame(
        [[qual, area, garage, bsmt, year, bath]],
        columns=columns
    )

    prediction = model.predict(X)[0]

    st.success(f"Estimated Price: ${prediction:,.0f}")

# Feature importance
st.subheader("📊 Feature Importance")

importance = pd.Series(
    model.feature_importances_,
    index=columns
).sort_values(ascending=False)

st.bar_chart(importance)