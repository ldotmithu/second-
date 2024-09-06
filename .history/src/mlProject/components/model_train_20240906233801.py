from mlProject.config.configuration import *
import pandas as pd 


class ModelTrain:
    def __init__(self,config:ModelTrainConfig) -> None:
        config=self.config
        
    def train_test_split(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data= pd.read_csv(self.config.test_data_path)
        
        target_col='quality'
        
        X_train=train_data.drop([target_col],axis=1)
        y_train=train_data[[target_col]]
        X_test=test_data.drop([target_col],axis=1)
        y_test=test_data[[target_col]]
        
        
        
        
        