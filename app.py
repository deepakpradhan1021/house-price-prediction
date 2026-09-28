import streamlit as st
import joblib
import pandas as pd

model = joblib.load('model.pkl')
st.title('House Price Predictor')

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