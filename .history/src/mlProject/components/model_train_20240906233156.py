from mlProject.config.configuration import *
import pandas as pd 

class ModelTrain:
    def __init__(self,config:ModelTrainConfig) -> None:
        config=self.config
        
    def train_test_split(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_csv= pd.read_csv(self.config.test_data_path)
        
        