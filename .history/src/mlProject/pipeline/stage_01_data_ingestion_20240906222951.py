from mlProject.entity.config_entity import *
from mlProject.config.configuration import *
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logging

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            Config=ConfigurationManager()
            data_ingestion_config=Config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_file()
            
        except Exception as e:
            logging.exception(e)
            raise e 