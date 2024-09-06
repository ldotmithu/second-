from src.mlProject.config.configuration import *
from src.mlProject.components.model_evaluation import *

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        Config=ConfigurationManager()
        model_evaluation_config=Config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.save_metics()