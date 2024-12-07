# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
#loading the saved model
loaded_model = pickle.load(open('C:/Users/muruga/Downloads/MLpart 5/trained_model.sav','rb'))
input_data = (4,110,92,0,0,37.6,0.191,30)
input_data_as_array = np.asarray(input_data)
input_data_reshaped = input_data_as_array.reshape(1,-1)
prediction =loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0] == 0):
  print("The person is not diabetic")
else:
  print("The person is diabetic")