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
```
## Feature Engineering

For feature engineering, categorical and numerical columns were processed as follows:

1. **Categorical Columns**: Encoded using one-hot encoding for each unique category to convert them into binary columns.
2. **Numerical Columns**: Standardized using a `StandardScaler` to normalize the data, ensuring numerical stability for the model.
   
   The resulting feature set allowed the model to work effectively with both categorical and continuous data types.

### Columns Used
The columns selected for training included weather-related variables such as temperature, humidity, wind speed, and cloud cover, which were most relevant for predicting rainfall. The key features were:

- **Location**: The city or town where the weather measurement was taken.
- **MinTemp** and **MaxTemp**: The minimum and maximum temperatures of the day.
- **Rainfall**: The amount of rain recorded for the day.
- **Evaporation** and **Sunshine**: Measures of evaporated water and hours of sunshine.
- **WindGustDir** and **WindGustSpeed**: The direction and speed of wind gusts.
- **Humidity**: Morning and afternoon humidity levels.
- **Pressure**: Atmospheric pressure readings.
- **Cloud**: Cloud cover in the morning and afternoon.
- **Temp9am** and **Temp3pm**: Temperatures recorded at 9 a.m. and 3 p.m.
- **RainToday**: Whether it rained the day before.

## Hyperparameter Tuning

The model's hyperparameters were optimized to improve accuracy and generalization. Key parameters tuned included:
- **n_estimators**: Set to 100, balancing between prediction accuracy and training time.
- **max_depth**: Limited to 8 to avoid overfitting, ensuring the model remains generalizable.
- **min_samples_split** and **min_samples_leaf**: Set to 2 to ensure that each split contains at least two samples.

These parameters were selected after several trials to achieve a good balance of accuracy and computational efficiency.

## Performance Metrics

In addition to accuracy, the following performance metrics were used to evaluate the model:
- **Precision**: Evaluates the proportion of true positive predictions out of all positive predictions.
- **Recall**: Measures the proportion of actual positives that were correctly identified.
- **F1-Score**: The harmonic mean of precision and recall, providing a balance between both metrics.
  
The final model achieved:
- **Accuracy Validation**: 84.1%
- **Accuracy Test**: 82.79%

## Data Visualization

Exploratory Data Analysis (EDA) was conducted to gain insights into the data and relationships between weather variables. Some key visualizations included:
- **Temperature Distributions**: Histograms of temperature values across different locations.
- **Rainfall Patterns**: Scatter plots showing rainfall across various regions and time periods.
- **Correlation Matrix**: Heatmap showing correlations between numerical features, highlighting relationships that may impact rainfall predictions.

Example visualizations are included in the `notebooks/EDA.ipynb` file for further exploration.

---

## How to Contribute

If you’re interested in improving this project, follow these steps:
1. **Fork** the repository.
2. **Clone** your forked repo locally.
3. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit them with a clear message.
5. Push your branch to your forked repo:
  ```bash
  git push origin feature-name
```
6. Open a Pull Request for review.
