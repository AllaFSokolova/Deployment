# Aussie Rain Prediction App 🌧️☀️

This repository contains a weather prediction app built with Python, Streamlit, and machine learning techniques. The model predicts whether it will rain tomorrow based on historical weather data in Australia. The model achieved an **Accuracy Validation** of **84.1%** and an **Accuracy Test** of **82.79%**.

## Project Structure
- `weatherAUS.csv`: The dataset containing historical weather data in Australia.
- `aussie_rain_pipeline.joblib`: The saved model pipeline for predicting rain.
- `app.py`: The main Streamlit app that loads the model and allows for user input to make predictions.

## Dependencies
This project requires the following Python libraries:
- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `joblib`
- `streamlit`

Install dependencies with:
```bash
pip install -r requirements.txt
