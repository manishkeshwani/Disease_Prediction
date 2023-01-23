# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

lepto_dataset = pd.read_csv('D:\Disease_Dectection\Leptospirosis.csv')

X = lepto_dataset.drop(columns = 'outcome',axis = 1)
Y = lepto_dataset['outcome']

X_train , X_test , Y_train , Y_test = train_test_split(X,Y , test_size=0.2, stratify=Y ,random_state=2)

model = LogisticRegression()

model.fit(X_train.values,Y_train.values) 

def lepto_prediction(input_data):
   
    array = np.asarray(input_data)
    reshaped_array = array.reshape(1,-1)
    prediction = model.predict(reshaped_array)
    
    if(prediction[0] == 1):
        return "you are probably suffering from Leptospirosis"
    else:
        return "you are safe"
