import streamlit as st
import numpy as np
import pandas as pd
import datetime
import requests


st.write('hello 👋')
'''
# TaxiFareModel front
'''

date = st.date_input('date', datetime.date(2019, 7, 6))
time= st.time_input('time', datetime.time(8, 45))
date_time = f"{date} {time}UTC"
pickup_longitude = st.number_input('pickup longitude', 0)
pickup_latitude = st.number_input("pickup latitude", 0)
dropoff_longitude = st.number_input("dropoff longitude", 0)
dropoff_latitude = st.number_input("dropoff latitude", 0)
passenger_count = st.number_input("passenger_count", 0)


params= dict(
        pickup_datetime=date_time,
        pickup_longitude=pickup_longitude,
        pickup_latitude=pickup_latitude,
        dropoff_longitude=dropoff_longitude,
        dropoff_latitude=dropoff_latitude,
        passenger_count=passenger_count)

#

url = 'https://violons-kdwmcasooa-ew.a.run.app/predict_fare/?'

result = requests.get(url, params=params)
#st.write(result.headers)
#predict = result[0]
json = result.json()
st.write('The fare will be', json['prediction'], '$')




