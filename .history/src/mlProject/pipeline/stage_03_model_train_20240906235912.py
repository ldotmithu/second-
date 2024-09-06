from mlProject.config.configuration import *
from mlProject.components.model_train import *

class ModelTrainPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        Config=ConfigurationManager()
        model_training_config=Config.get_model_train_config()
        model_training=ModelTrain(config=model_training_config)
        model_training.train_test_split()