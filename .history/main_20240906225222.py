from src.mlProject.pipeline.stage_01_data_ingestion import *
from src.mlProject.pipeline.stage_02_data_transfomation import *
from src.mlProject import logging

Stage_name='Data Ingestion'

try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info('Data Ingestion Complate')
    
except Exception as e:
    logging.exception(e)
    raise e    


Stage_name='Data Transfomation'

try:
    data_transfomation=DataTransfomationPipelone()
    data_transfomation.main()
    logging.info('Data Ingestion Complate')
    
except Exception as e:
    logging.exception(e)
    raise e  