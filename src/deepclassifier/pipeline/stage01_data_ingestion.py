
from deepclassifier.components.dataingestion import DataIngestionComponent
from deepclassifier.config import ConfigurationManager
from deepclassifier import logger

START_STAGE="Data Ingestion Stage"
def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestionComponent(config=data_ingestion_config)
    data_ingestion.download_files()
    data_ingestion.unzip_and_clean()

if __name__ == "__main__":
    try:
        logger.info(f"\n\nSTAGE {START_STAGE}>>>>>>>>>> has started <<<<<<<<<<<")
        main()
        logger.info(f"STAGE {START_STAGE}>>>>>>>>>> has Ended   <<<<<<<<<<<\n\nX==============X")
    except Exception as e:
        logger.exception(e)
        raise e