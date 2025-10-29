import pandas as pd 
import numpy as np 
import pickle
import json
import warnings
warnings.filterwarnings("ignore")

import config

class DaibeticPred_class():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age
        
        
        
    def model_load(self):
        
        with open(config.json_file,'r') as f:
            self.JSON = json.load(f)
            
        #pickle 
        with open(config.model_file,'rb') as f:
            self.model = pickle.load(f)
            
            
            
    def predict_output(self):
        
        self.model_load()
        
        array = np.array([self.Glucose,self.BloodPressure,self.SkinThickness,self.Insulin,self.BMI,self.DiabetesPedigreeFunction,self.Age],ndmin=2)
        
        
        predict = self.model.predict(array)
        
        print("final output is-------",predict)
        
        # if predict[0] == 1 :                      # because predict return array
        #     A = "petiant is not diabetic********"
            
        # else:
        #     A = "petiant is diabetics***************"
            


        return ["petiant is not diabetic********", "petiant is diabetics***************"][predict[0]]


Glucose = 107.000
BloodPressure = 50.000
SkinThickness = 35.000
Insulin = 0.000
BMI = 33.600
DiabetesPedigreeFunction = 0.627
Age = 50.000       
        
obj = DaibeticPred_class(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        
predict = obj.predict_output()
print("***output is *****",predict)