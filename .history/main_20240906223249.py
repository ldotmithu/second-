from src.mlProject.pipeline.stage_01_data_ingestion import *
from src.mlProject import logging

Stage_name='Data Ingestion'

try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info('Data Ingestion Complate')
    
except Exception as e:
    logging.exception(e)
    raise e    