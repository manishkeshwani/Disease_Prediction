# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from dengue_model import dengue_prediction
from lepto_model import lepto_prediction
from charts import pie,bar,hbar,scatter
from dataAnalysis import lepto_dataAnalysis,dengue_dataAnalysis
from weather import weatherfunc
from weather import func



#for conversion of yes into 1 and no into 0
def variables(var,data_list):
    if(var == 'Yes'):
        data_list.append(1)
    if(var == 'No'):
        data_list.append(0)
    

#dengue funtion
def dengue():
    
    select1 = st.selectbox("ABOUT DENGUE",['Dengue Prediction','Dengue Analysis'])    
    
    #dengue prediction
    if(select1 == 'Dengue Prediction'):
        
        st.header('Dengue Prediction')
        
        lst = [" ","Yes","No"]
        feverlst=["",96,97,98,99,100,101,102,103,104,105,106]
        col_1 , col_2 = st.columns(2)

        # getting the input data from the user
        with col_1:
            fever = st.selectbox('Fever(°F)',feverlst)
            headache = st.selectbox('Headache',lst)
            eye_pain = st.selectbox('Pain Behind Eyes',lst)
            ache = st.selectbox('Joint or Muscle Ache',lst)
            taste = st.selectbox('Change In Taste',lst)
        with col_2:
            appetite_loss = st.selectbox('Appetite Loss',lst)
            stomach_ache = st.selectbox('Abdominal Pain',lst)
            vomatting = st.selectbox('Nausea or Vomatting',lst)
            diarrhoea = st.selectbox('Diarrhoea',lst)
        
        # code for prediction
        diagnosis = ''
        dengue_list = [fever]
        
        #headache converting to 0 or 1
        variables(headache,dengue_list)
            
        #eye_pain converting to 0 or 1
        variables(eye_pain,dengue_list)
            
        #ache converting to 0 or 1
        variables(ache,dengue_list)
        
        #taste converting to 0 or 1
        variables(taste,dengue_list)
            
        #appetite_loss converting to 0 or 1
        variables(appetite_loss,dengue_list)
                    
        #stomach_ache converting to 0 or 1
        variables(stomach_ache,dengue_list)
             
        #vomatting converting to 0 or 1
        variables(vomatting,dengue_list)
        
        #diarrhoea converting to 0 or 1
        variables(diarrhoea,dengue_list)       
               
            
        #creating a button for prediction
        if st.button("Predict"):               
            diagnosis = dengue_prediction(dengue_list)

        # for printing result checking the condition       
        if(diagnosis == 0):
            st.success("you are safe")
        if(diagnosis == 1):
            st.error("You are probably affected with dengue!!!")
        
        # for precautions
        if st.button("Precautions"):
            st.header("Precautions of Dengue")
            st.warning("Cover your skin by wearing long pants, and long-sleeved shirts.")
            st.warning("Use of mosquito repellents, traps, and nets.")
            st.warning("Wear closed footwear")
            st.warning("Keep all the doors and windows closed especially at dawn, dusk, and early evening to avoid the entry of Dengue mosquitoes.")
            st.warning("Keep your surroundings clean by removing all the waste and cleaning the standing water.")
       

            
            
    # Dengue Analysis
    else:
        
        st.header('Dengue Analysis')
        state = st.selectbox("Select Location of India",[" ",'Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir',
                                                          'Jharkhand','Karnataka','Kerala','Lakshadweep','Madhya Pradesh','Meghalaya','Maharashtra','Manipur','Mizoram','Nagaland','Odisha',
                                                          'Punjab','rajasthan','sikkim','Tamil Nadu','Tripura','Telangana','Uttar Pradesh','Uttarakhand','West Bengal','Andaman & Nicobar Islands',
                                                          'Chandigarh','Delhi','Dadra & Nagar Haveli','Daman & Diu','Puducherry'])
    
        year = st.selectbox("Year",[" ",'2017','2018','2019','2020','2021','2022'])
        
        case_death = st.selectbox("Cases or Deaths",["",'Cases','Deaths'])
        
        
        if(case_death=='Cases'):
            res = dengue_dataAnalysis.loc[state, year+case_death]
        if(case_death=='Deaths'):
            res = dengue_dataAnalysis.loc[state, year+case_death]
            
        col_1 , col_2 = st.columns(2)
        
        with col_1:
            if st.button("Data Analysis"):
                if(case_death =='Cases'):
                    st.header("Cases")
                    st.write("Total Number of Cases in",state,"in",year,"is",res)
                if(case_death =='Deaths'):
                    st.header("Deaths")
                    st.write("Total Number of People Died in",state,"in",year,"is",res)
                
                #dengue report on basis of weather
                st.subheader("Dengue Report on the Basis of Current Weather")
                func(state)
                #precautions of dengue
                st.subheader("Precautions of Dengue")
                st.warning("Cover your skin by wearing long pants, and long-sleeved shirts.")
                st.warning("Use of mosquito repellents, traps, and nets.")
                st.warning("Wear closed footwear")
                st.warning("Keep all the doors and windows closed especially at dawn, dusk, and early evening to avoid the entry of Dengue mosquitoes.")
                st.warning("Keep your surroundings clean by removing all the waste and cleaning the standing water.")

                # weather report for more details
                st.subheader("Current Weather Report For More Details")
                weatherfunc(state)
                
                
        with col_2:            
            charts = st.selectbox("Visual Analysis",["",'Pie Chart','Bar Chart','Horizontal Bar Chart','Scatter Chart'])
            
            if(charts == 'Pie Chart'):
                pie(state,year,dengue_dataAnalysis)
            
            if(charts == 'Bar Chart'):
                bar(state,year,dengue_dataAnalysis)
               
                
            if(charts == 'Horizontal Bar Chart'):
                hbar(state,year,dengue_dataAnalysis)
                
                
            if(charts == 'Scatter Chart'):
                scatter(state,year,dengue_dataAnalysis)
                   
#leptospirosis funtion
def lepto():
      
    select2 = st.selectbox("ABOUT LEPTOSPIROSIS",['leptospirosis Prediction','leptospirosis Analysis'])    
    
    #leptospirosis prediction
    if(select2 == 'leptospirosis Prediction'):
        
        st.header('Leptospirosis Prediction')

        # getting the input data from the user
        lst = [" ","Yes","No"]
        feverlst=["",96,97,98,99,100,101,102,103,104,105,106]
        
        col_1 , col_2 = st.columns(2)
        
        with col_1:
            fever2 = st.selectbox('Fever(°F)',feverlst)
            headache2 = st.selectbox('Headache',lst)
            ache2 = st.selectbox('Joint or Muscle Ache',lst)
            vomatting2 = st.selectbox('Nausea or Vomatting',lst)
            red_eye = st.selectbox('Red Eyes',lst)
        with col_2:
            coughing_blood = st.selectbox('Blood in Coughing',lst)
            chills = st.selectbox('Chills or Shivering',lst)
            diarrhoea2 = st.selectbox('Diarrhoea',lst)
            stomach_ache = st.selectbox('Abdominal Pain',lst)
        
        
        # code for prediction
        diagnosis=''
        lepto_list = [fever2]
        
        #headache2 converting to 0 or 1
        variables(headache2,lepto_list)                
            
        #ache2 converting to 0 or 1
        variables(ache2,lepto_list)
            
        #vomatting2 converting to 0 or 1
        variables(vomatting2,lepto_list)
            
        #red_eye converting to 0 or 1
        variables(red_eye,lepto_list)
            
        #coughing_blood converting to 0 or 1
        variables(coughing_blood,lepto_list)
            
        #chills converting to 0 or 1
        variables(chills,lepto_list)
                        
        #diarrhoea converting to 0 or 1
        variables(diarrhoea2,lepto_list)
        
        #stomach_ache converting to 0 or 1
        variables(stomach_ache,lepto_list)
        
        #creating a button for prediction
        if st.button("Predict"):
            diagnosis = lepto_prediction(lepto_list)
            
        # for result and checking condition for leptospirosis
        if(diagnosis == "you are safe"):
            st.success(diagnosis)
        else:
            st.error(diagnosis)  

        if st.button("Precautions"):
            st.header("Precautions of Leptospirosis")
            st.warning("Avoid walking through stagnant water")
            st.warning("Wear closed footwear")
            st.warning("Dress all your wounds and cuts")
            st.warning("If you have walked through stagnant water, wash your arms and legs with soap and water.")


    #leptospirosis analysis
    else:
        st.header("leptospirosis Analysis")

        country = st.selectbox("Country",['India'])    
        year2 = st.selectbox("Year",[" ",'2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'])
        case_death2 = st.selectbox("Cases or Deaths",["",'Cases','Deaths'])
        
        
        if(case_death2=='Cases'):
            res2 = lepto_dataAnalysis.loc[country, year2 + case_death2]
        if(case_death2 == 'Deaths'):
            res2 = lepto_dataAnalysis.loc[country, year2 + case_death2]
            
        col_1 , col_2 = st.columns(2)
        
        with col_1:
            if st.button("Data Analysis"):
                if(case_death2 =='Cases'):
                    st.header("Cases")
                    st.write("Total Number of Cases in",country,"in",year2,"is",res2)
                if(case_death2=='Deaths'):
                    st.header("Deaths")
                    st.write("Total Number of People Died in",country,"in",year2,"is",res2)
                #dengue report on basis of weather
                st.subheader("Leptospirosis Report on the Basis of Current Weather")
                func(country)
                #precautions of Leptospirosis
                st.subheader("Precautions of Leptospirosis")
                st.warning("Avoid walking through stagnant water")
                st.warning("Wear closed footwear")
                st.warning("Dress all your wounds and cuts")
                st.warning("If you have walked through stagnant water, wash your arms and legs with soap and water.")
                #weather report for more details
                st.subheader("Current Weather Report For More Details")
                weatherfunc(country)
                
                
        with col_2:            
            charts = st.selectbox("Visual Analysis",["",'Pie Chart','Bar Chart','Horizontal Bar Chart','Scatter Chart'])
            
            if(charts == 'Pie Chart'):
                pie(country,year2,lepto_dataAnalysis)
            
            if(charts == 'Bar Chart'):
                bar(country,year2,lepto_dataAnalysis)              
                
            if(charts == 'Horizontal Bar Chart'):
                hbar(country,year2,lepto_dataAnalysis)
                              
            if(charts == 'Scatter Chart'):
                scatter(country,year2,lepto_dataAnalysis)
                

with st.sidebar:
    selected = option_menu(menu_title = "Disease Prediction System",
                           
                           options=['Dengue Prediction','Leptospirosis Prediction'],
                           
                           icons=['activity','activity'],
                           
                           menu_icon = 'cast',
                                                     
                           orientation = 'vertical',
                           
                           default_index = 0)


# Dengue page   
if(selected == 'Dengue Prediction'):
    st.title('Dengue Prediction & Analysis System')
    dengue()

# leptospirosis page    
if(selected == 'Leptospirosis Prediction'):
    st.title('Leptospirosis Prediction & Analysis System')
    lepto()