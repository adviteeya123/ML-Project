# directory in which we will log this file
from datetime import datetime
from distutils.log import INFO
import logging
import os
from tkinter import CURRENT
import os
from tkinter.tix import Tree
LOG_DIR = "housing_logs"

# within log folder we will create file name
# so when we trigger file at particualr time sampt is created

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
LOG_FILE_NAME= f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR, exist_ok= True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename= LOG_FILE_PATH
filemode= 'w',
format= '[%(asctime)s] %(levelname)s - %(message)s',
level= logging.INFO

)

