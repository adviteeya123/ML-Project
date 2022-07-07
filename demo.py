
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #data_ingestion_config = Configuartion().get_data_ingestion_config()
        #data_validation_config = Configuartion().get_data_validation_config()
        #data_transformation_config = Configuartion().get_data_transformation_config()
        #data_model_training_config = Configuartion().get_model_trainer_config()
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()

