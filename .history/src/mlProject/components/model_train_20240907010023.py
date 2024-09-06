from mlProject.config.configuration import *
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
import joblib
from mlProject import logging
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
        
    def preprocess(self):
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
            
        
    def train(self):
    
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
     
        target_col = 'quality'
        
        
        X_train = train_data.drop(columns=[target_col])
        X_test = test_data.drop(columns=[target_col])
        y_train = train_data[target_col]
        y_test = test_data[target_col]
        
        
        rf = RandomForestRegressor(
            n_estimators=1000,
            criterion='squared_error',
            max_depth=6,
            min_samples_split=4,
            min_samples_leaf=2,
            max_features='sqrt',
            bootstrap=True,
            n_jobs=-1,
            random_state=42
        )
        
        rf.fit(X_train, y_train)
        
        joblib.dump(rf,os.path.join(self.config.root_dir,self.config.model_name))
        

        
        
        
        