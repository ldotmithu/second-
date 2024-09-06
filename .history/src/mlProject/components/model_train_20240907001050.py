from mlProject.config.configuration import *
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
import joblib


class ModelTrain:
    def __init__(self,config:ModelTrainConfig):
        self.config=config
        
    def train_test_split(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data= pd.read_csv(self.config.test_data_path)
        
        target_col='quality'
        
        X_train=train_data.drop([target_col],axis=1)
        y_train=train_data[target_col]
        X_test=test_data.drop([target_col],axis=1)
        y_test=test_data[target_col]
        
        rf=RandomForestRegressor()
        rf.fit(X_train,y_train)
        
        model_dir = os.path.join(self.config.root_dir, 'artifacts', 'model_training')
        os.makedirs(model_dir, exist_ok=True)
        
        model_path = os.path.join(model_dir, self.config.model_name)
        joblib.dump(rf, model_path)
        
        
        
        
        