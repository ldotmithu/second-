from mlProject.config.configuration import *
from sklearn.metrics import r2_score

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig) -> None:
        self.config=config
        
    def eval_metics(self,actual,pred):
        r2_sco=r2_score(actual,pred)
        
        return r2_sco
    
    def save_metics(self):
        test_data=
            