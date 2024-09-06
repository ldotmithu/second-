from mlProject.config.configuration import *
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression,ElasticNet
import joblib
from mlProject import logging
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVR
from sklearn.ensemble import E
class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
        
    def preprocess_task(self):
        num_col=['fixed acidity',
 'volatile acidity',
 'citric acid',
 'residual sugar',
 'chlorides',
 'free sulfur dioxide',
 'total sulfur dioxide',
 'density',
 'pH',
 'sulphates',
 'alcohol']
        
        num_pipeline=Pipeline([
            ('scaler',StandardScaler())
        ])
        preprocess=ColumnTransformer([
            ('num_pipeline',num_pipeline,num_col)
        ])
        
        return preprocess
            
        
    def train(self):
    
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
     
        target_col = 'quality'
        
        
        X_train = train_data.drop(columns=[target_col])
        X_test = test_data.drop(columns=[target_col])
        y_train = train_data[target_col]
        y_test = test_data[target_col]
        
        preprocess_obj=self.preprocess_task()
        
        X_train=preprocess_obj.fit_transform(X_train)
        X_test=preprocess_obj.fit(X_test)
        
        
        elr = ElasticNet()
        
        elr.fit(X_train, y_train)
        
        joblib.dump(elr,os.path.join(self.config.root_dir,self.config.model_name))
        

        
        
        
        