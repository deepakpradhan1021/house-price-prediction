import streamlit as st
import joblib
import pandas as pd

def inr(lakhs):
    return f'₹{lakhs/100:.2f} Crore' if lakhs >= 100 else f'₹{lakhs:.1f} Lakh'

st.title('House Price Predictor')
market = st.sidebar.radio('Choose market', ['🇮🇳 India (Bengaluru, ₹)', '🇺🇸 USA (Ames, $)'])

if market.startswith('🇮🇳'):
    data = joblib.load('model_india.pkl')
    model, locations = data['model'], data['locations']
    loc = st.selectbox('Location', locations)
    sqft = st.number_input('Area (sq ft)', 300, 10000, 1200)
    bhk = st.slider('BHK', 1, 8, 2)
    bath = st.slider('Bathrooms', 1, 8, 2)
    if st.button('Predict'):
        X = pd.DataFrame([[loc, sqft, bath, bhk]], columns=['location','total_sqft','bath','bhk'])
        st.success(f'Estimated price: {inr(model.predict(X)[0])}')
else:
    model = joblib.load('model.pkl')
    qual = st.slider('Overall Quality (1-10)', 1, 10, 5)
    area = st.number_input('Living Area (sq ft)', 500, 6000, 1500)
    garage = st.slider('Garage Capacity (cars)', 0, 4, 2)
    bsmt = st.number_input('Basement Area (sq ft)', 0, 4000, 800)
    year = st.number_input('Year Built', 1870, 2010, 1990)
    bath = st.slider('Full Bathrooms', 0, 4, 2)
    if st.button('Predict'):
        cols = ['OverallQual','GrLivArea','GarageCars','TotalBsmtSF','YearBuilt','FullBath']
        X = pd.DataFrame([[qual, area, garage, bsmt, year, bath]], columns=cols)
        st.success(f'Estimated price: ${model.predict(X)[0]:,.0f}')