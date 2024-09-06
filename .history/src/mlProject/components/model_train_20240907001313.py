from mlProject.config.configuration import *
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
import joblib
from mlProject import logging

class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
    def train_test_split(self):
        try:
            train_data=pd.read_csv(self.config.train_data_path)
            test_data= pd.read_csv(self.config.test_data_path)
            
            target_col='quality'
            
            X_train=train_data.drop([target_col],axis=1)
            y_train=train_data[target_col]
            X_test=test_data.drop([target_col],axis=1)
            y_test=test_data[target_col]
            
            rf=RandomForestRegressor()
            rf.fit(X_train,y_train)
            
            
            joblib.dump(rf,os.path.join(self.config.root_dir,self.config.model_name))
        except Exception as e:
            logging.exception(e)
            raise e 
        
        
        
        