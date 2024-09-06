from mlProject.config.configuration import *
from sklearn.metrics import r2_score
import pandas as pd 
import joblib,json
from pathlib import Path

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig) -> None:
        self.config=config
        
    def eval_metics(self,actual,pred):
        r2_sco=r2_score(actual,pred)
        
        return r2_sco
    
    def save_metics(self):
        test_data=pd.read_csv(self.config.test_data_path)
        target_col='quality'
        
        X_test=test_data.drop(columns=[target_col],axis=1)
        y_test=test_data[target_col]
        model=joblib.load(self.config.model_path)
        
        predication=model.predict(X_test)
        
        score=self.eval_metics(predication,y_test)
        
        
        save_json(path=Path(self.config.metrics_name),data=score)
        
        print(score)
        
            