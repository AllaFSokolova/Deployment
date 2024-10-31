import streamlit as st
import numpy as np
import pandas as pd  # Import pandas for DataFrame
import joblib

def predict(location, mintemp, maxtemp, 
            rainfall, evaporation, sunshine, 
            windgustdir, windgustspeed, winddir9am, 
            winddir3pm, windspeed9am, windspeed3pm, 
            humidity9am, humidity3pm, pressure9am, 
            pressure3pm, cloud9am, cloud3pm, temp9am, 
            temp3pm, raintoday):
    
    model = joblib.load('aussie_rain_pipeline.joblib')
    
    # Create a DataFrame from the input data
    data = pd.DataFrame({
        'Location': [location],
        'MinTemp': [mintemp],
        'MaxTemp': [maxtemp],
        'Rainfall': [rainfall],
        'Evaporation': [evaporation],
        'Sunshine': [sunshine],
        'WindGustDir': [windgustdir],
        'WindGustSpeed': [windgustspeed],
        'WindDir9am': [winddir9am],
        'WindDir3pm': [winddir3pm],
        'WindSpeed9am': [windspeed9am],
        'WindSpeed3pm': [windspeed3pm],
        'Humidity9am': [humidity9am],
        'Humidity3pm': [humidity3pm],
        'Pressure9am': [pressure9am],
        'Pressure3pm': [pressure3pm],
        'Cloud9am': [cloud9am],
        'Cloud3pm': [cloud3pm],
        'Temp9am': [temp9am],
        'Temp3pm': [temp3pm],
        'RainToday': [raintoday]
    })
    
    # Make predictions using the DataFrame
    predictions = model.predict(data)
    return predictions[0]

# Заголовок застосунку
st.title('Прогнозування дощу в Австралії')
st.image('meteo.jpg', caption='Weather Forecast Image', use_column_width=True)
st.markdown('Це проста модель для прогнозу чи буде дощ завтра чи ні')

# Assuming you have your dataset loaded from a CSV file
weather_df = pd.read_csv("weatherAUS.csv") 

# Відображення таблиці середніх значень для числових змінних
st.header("Середні значення кількісних характеристик для кожного типу дощу")
numeric_cols = weather_df.select_dtypes(include='number').columns  # Select only numeric columns
mean_values = weather_df.groupby('RainToday')[numeric_cols].mean().reset_index()
st.dataframe(mean_values)

st.markdown('Введіть дані:') 

locations = np.array(['Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree',
                      'Newcastle', 'NorahHead', 'NorfolkIsland', 'Penrith', 'Richmond',
                      'Sydney', 'SydneyAirport', 'WaggaWagga', 'Williamtown',
                      'Wollongong', 'Canberra', 'Tuggeranong', 'MountGinini', 'Ballarat',
                      'Bendigo', 'Sale', 'MelbourneAirport', 'Melbourne', 'Mildura',
                      'Nhil', 'Portland', 'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns',
                      'GoldCoast', 'Townsville', 'Adelaide', 'MountGambier', 'Nuriootpa',
                      'Woomera', 'Albany', 'Witchcliffe', 'PearceRAAF', 'PerthAirport',
                      'Perth', 'SalmonGums', 'Walpole', 'Hobart', 'Launceston',
                      'AliceSprings', 'Darwin', 'Katherine', 'Uluru'])

wind_directions = ['W', 'WNW', 'WSW', 'NE', 'NNW', 'N', 'NNE', 'SW', 'ENE', 
                   'SSE', 'S', 'NW', 'SE', 'ESE', 'E', 'SSW']
rain_today_options = ['Yes', 'No']

# Інтерфейс для введення даних
location = st.selectbox('location', locations)
mintemp = st.number_input('mintemp', value=15.0)
maxtemp = st.number_input('maxtemp', value=25.0)
rainfall = st.number_input('rainfall', value=0.0)
evaporation = st.number_input('evaporation', value=5.0)
sunshine = st.number_input('sunshine', value=8.0)
windgustdir = st.selectbox('windgustdir', wind_directions)
windgustspeed = st.number_input('windgustspeed', value=30)
winddir9am = st.selectbox('winddir9am', wind_directions)
winddir3pm = st.selectbox('winddir3pm', wind_directions)
windspeed9am = st.number_input('windspeed9am', value=10)
windspeed3pm = st.number_input('windspeed3pm', value=15)
humidity9am = st.number_input('humidity9am', value=70)
humidity3pm = st.number_input('humidity3pm', value=65)
pressure9am = st.number_input('pressure9am', value=1015.0)
pressure3pm = st.number_input('pressure3pm', value=1010.0)
cloud9am = st.number_input('cloud9am', value=3)
cloud3pm = st.number_input('cloud3pm', value=4)
temp9am = st.number_input('temp9am', value=18.0)
temp3pm = st.number_input('temp3pm', value=22.0)
raintoday = st.selectbox('raintoday', rain_today_options)

# Кнопка для прогнозування
if st.button('прогнозувати'):
    prediction = predict(location, mintemp, maxtemp, 
                         rainfall, evaporation, sunshine, 
                         windgustdir, windgustspeed, winddir9am, 
                         winddir3pm, windspeed9am, windspeed3pm, 
                         humidity9am, humidity3pm, pressure9am, 
                         pressure3pm, cloud9am, cloud3pm, temp9am, 
                         temp3pm, raintoday)
    
    st.write('результат прогнозу:', 'так' if prediction == 1 else 'ні')



