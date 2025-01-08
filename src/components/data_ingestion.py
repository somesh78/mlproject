import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('atrifacts', "train.csv")
    test_data_path: str=os.path.join('atrifacts', "test.csv")
    raw_data_path: str=os.path.join('atrifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_ingestion(self):
        logging.info("Entered the data ingestion or component")
        try:
            df=pd.read_csv('Notebooks\StudentsPerformance.csv')
            logging.info('Read the dataset as a dataframe')

            os.makedirs(self.ingestion_config.train_data_path)
        except:
            pass
    