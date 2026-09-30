# 🏠 House Price Prediction

A machine learning project that predicts house prices for both **USA and India (Bengaluru)** using different real-world housing datasets.

## 🚀 Live Demo

🔗 [Try the House Price Prediction App](https://house-price-prediction-isncgvvwk89mvcahtd33rr.streamlit.app/)

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Random Forest
- Gradient Boosting
- Streamlit
- Git & GitHub

## Project Workflow

1. Loaded and explored housing datasets
2. Performed Exploratory Data Analysis (EDA)
3. Handled missing values
4. Removed outliers where required
5. Performed feature engineering
6. Encoded categorical features
7. Trained Machine Learning regression models
8. Evaluated models using MAE and R²
9. Deployed the models using Streamlit

## Model Performance

### 🇺🇸 USA — Ames Housing Dataset

- Model: Random Forest Regressor
- MAE: ~17,454
- R² Score: ~0.89

### 🇮🇳 India — Bengaluru Housing Dataset

- Model: Gradient Boosting Regressor
- R² Score: ~0.79

## Project Files

- `app.py` — Streamlit web application
- `analysis.ipynb` — USA data analysis, preprocessing and model training
- `india_model.ipynb` — India data analysis, preprocessing and model training
- `model.pkl` — Trained USA model
- `model_india.pkl` — Trained India model
- `data/` — Dataset files
- `requirements.txt` — Python dependencies
- `.gitignore` — Files excluded from Git

## 🌐 Application Features

- 🇺🇸 USA house price prediction
- 🇮🇳 Bengaluru house price prediction
- 💵 USD and ₹ currency support
- Interactive Streamlit interface
- Input validation
- Feature-based price prediction

## Conclusion

This project helped me understand the complete Machine Learning workflow, from data cleaning and exploratory analysis to model training, evaluation, and deployment.

The USA Random Forest model achieved an R² score of approximately **0.89**, while the Bengaluru Gradient Boosting model achieved approximately **0.79**.

## Dataset

- [Kaggle House Prices — USA](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview)
- Kaggle Bengaluru House Price Dataset
