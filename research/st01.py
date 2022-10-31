from fileinput import filename
import os
import urllib.request as request
from zipfile import ZipFile
from collections import namedtuple


from deepclassifier.constants import *
from deepclassifier.utils.common import read_yaml, create_directories

os.chdir("../")

DataIngestionConfig=namedtuple("DataIngestionConfig",[
    "root_dir",
    "source_URL",
    "local_data_file",
    "unzip_dir"
])

class ConfigurationManager:
    def __init__(self,
        config_file_path=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
        return data_ingestion_config

        
class DataIngestionComponent:
    def __init__(self,config: DataIngestionConfig):
        self.config=config
    
    def download_files(self): # will downaload as data.zip file
        if not os.path.exists(self.config.local_data_file):
            filename, header= request.urlretrieve(
                url= self.config.source_URL,
                filename=self.config.local_data_file
            )

    def _getupdated_list_of_files(self,list_of_files: list):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f )]

    def _clean(self, zipf: ZipFile, f: str, working_dir: str):
        target_file_path=os.path.join(working_dir,f)
        if not os.path.exists(target_file_path):
            f.extract(f, working_dir)

        if os.path.getsize(target_file_path) == 0:
            os.remove(target_file_path)

    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file,mode="r") as zipf:
            list_of_files=zipf.namelist()
            updated_list_of_files=self._getupdated_list_of_files(list_of_files)
            for f in updated_list_of_files:
                self._clean(zipf,f,self.unzip_dir)



try: 
    config=ConfigurationManager()
    data_ingestion_config=config.get_data_ingestion_config
    data_ingestion=DataIngestionComponent(config=data_ingestion_config)
    data_ingestion.download_files()
    data_ingestion.unzip_and_clean()
except Exception as e:
    raise e


