# we will be creating many functions in this configurartion file
import imp
from logging.config import fileConfig
from tkinter import E
from sklearn.linear_model import PassiveAggressiveClassifier

from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig,DataTransfromationConfig, DataValidationConfig, ModelEvaluationConfig, ModelPushConfig, ModelPusherConfig, ModelTrainerConfig, TrainingPipelineConfig,
ModelEvaluationConfig,ModelPusherConfig, TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.exception import HousingException
from  housing.constant import *
import sys,os









class Configuration:

    def __init__ (self,
        config_file_path:str= CONFIG_FILE_PATH,
        current_time_stamp: str = CURRENT_TIME_STAMP
          ) -> None:
         self.config_info = read_yaml_file(file_path = config_file_path)
         self.get_training_pipeline_config = self.get_training_pipeline_config()
         self.time_stamp = current_time_stamp

        

    def get_data_ingestion_config(self) -> DataIngestionConfig :
        pass
    def get_data_valiation_config(self) -> DataValidationConfig :
        pass
    def get_data_transformation_config(self) -> DataTransfromationConfig :
        pass
    def get_mode_trainer_config(self) -> ModelTrainerConfig:
        pass
    def get_model_evaluation_config(self) -> ModelEvaluationConfig :
        pass
    def get_model_push_pusher_config(self) -> ModelPusherConfig :
        pass
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
             
        except Exception as e:
            raise HousingException(e,sys) from e