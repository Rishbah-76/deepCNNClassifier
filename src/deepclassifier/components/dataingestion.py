from zipfile import ZipFile
import urllib.request as request
import os
from deepclassifier.entity import DataIngestionConfig
from pathlib import Path
from deepclassifier import logger
from deepclassifier.utils import get_size
from tqdm import tqdm

class DataIngestionComponent:
    def __init__(self,config: DataIngestionConfig):
        self.config=config
    
    def download_files(self): # will downaload as data.zip file
        logger.info(f"Trying to Download the DataZip file.....")
        if not os.path.exists(self.config.local_data_file):
            filename, header= request.urlretrieve(
                url= self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloading the data Zipfile {filename} with header : \n{header}")
        else:
            logger.info(f"Data Zipfile already exists of size: {get_size(Path(self.config.local_data_file))}")


    def _getupdated_list_of_files(self,list_of_files: list):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f )]

    def _clean(self, zipf: ZipFile, f: str, working_dir: str):
        target_file_path=os.path.join(working_dir,f)
        if not os.path.exists(target_file_path):
            zipf.extract(f, working_dir)

        if os.path.getsize(target_file_path) == 0:
            logger.info(f"removing file:{target_file_path} of size: {get_size(Path(target_file_path))}")
            os.remove(target_file_path)

    def unzip_and_clean(self):
        logger.info(f"unzipping file and removing unawanted files")
        with ZipFile(file=self.config.local_data_file,mode="r") as zipf:
            list_of_files=zipf.namelist()
            updated_list_of_files=self._getupdated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._clean(zipf,f,self.config.unzip_dir)
