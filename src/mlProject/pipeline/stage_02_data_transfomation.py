from mlProject.config.configuration import *
from mlProject.components.data_transfomation import *

class DataTransfomationPipelone:
    def __init__(self) -> None:
        pass
    
    def main(self):
        Config=ConfigurationManager()
        data_transfomation_config=Config.get_data_transfomtion_config()
        data_transfomation=DataTransfomation(config=data_transfomation_config)
        data_transfomation.split_data()