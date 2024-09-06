from src.mlProject.pipeline.stage_01_data_ingestion import *
from src.mlProject.pipeline.stage_02_data_transfomation import *
from src.mlProject.pipeline.stage_03_model_train import *
from src.mlProject.pipeline.stage_04_model_evaluation import *
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
    logging.info('Data transfomation Complate')
    
except Exception as e:
    logging.exception(e)
    raise e  


Stage_name='Model Train '

try:
    model_train=ModelTrainPipeline()
    model_train.main()
    logging.info('Model Train Complate')
    
except Exception as e:
    logging.exception(e)
    raise e  


Stage_name='Model Evaluation '

try:
    model_evaluation=ModelEvaluationPipeline()
    model_evaluation.main()
    logging.info('Model Evaluation Complate')
    
except Exception as e:
    logging.exception(e)
    raise e  