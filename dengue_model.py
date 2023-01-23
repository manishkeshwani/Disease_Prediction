# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

dengue_dataset = pd.read_csv("dengue.csv")

X = dengue_dataset.drop(columns = "outcome" , axis=1)
Y = dengue_dataset['outcome'] 

X_train , X_test , Y_train , Y_test = train_test_split(X,Y, test_size=0.2 ,stratify=Y,random_state=2)

model = LogisticRegression()


model.fit(X_train.values,Y_train.values)


def dengue_prediction(input_data):
    #prediction system
   
    
    array = np.asarray(input_data)
    
    reshaped_data_array = array.reshape(1,-1)
    
    prediction = model.predict(reshaped_data_array)
    #print(prediction)
    
    if (prediction[0] == 1):
      return 1
    else:
      return 0 

  

  
    

  
