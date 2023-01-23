# -*- coding: utf-8 -*-

import requests
import json
import streamlit as st


def func(cityname):
    apiKey = "4c9235f735a0cf8f193d9472cf663fcf"

    baseURL = "https://api.openweathermap.org/data/2.5/weather?q="



    completeURL = baseURL + cityname + "&appid=" + apiKey

    response = requests.get(completeURL)

    data = response.json()    
    if(data['weather'][0]['main']!='rain'):
        st.success('''According to Weather Report, Dengue is Less Spreading These Days, 
        But Taking Precautions is Always Better''')
    else:
        st.warning("Dengue is Spreading Take Precautions")


def weatherfunc (cityname):
    
    apiKey = "4c9235f735a0cf8f193d9472cf663fcf"

    baseURL = "https://api.openweathermap.org/data/2.5/weather?q="



    completeURL = baseURL + cityname + "&appid=" + apiKey

    response = requests.get(completeURL)

    data = response.json()
    
    st.write("Place :",data['name'])
    st.write("Country :",data['sys']['country'])
    st.write("Temperature :", data['main']['temp']-273.15,"°C")
    st.write("Maximum Temperature :", data['main']['temp_max']-273.15,"°C")
    st.write("Minimum Temperature :", data['main']['temp_min']-273.15,"°C")
    st.write("Weather :", data['weather'][0]['main'])
    st.write("Humidity :", data['main']['humidity'],"%")
    st.write("Visibility :", data['visibility'],"m")
    st.write("Wind Speed :", data['wind']['speed'],"km/h")
    


