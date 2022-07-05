from gc import get_referents
from unicodedata import name
from xml.etree.ElementTree import VERSION
from importlib_metadata import version
from setuptools import find_packages, setup
from typing import List





#DECLARING VARIABLES FOR SETUP FUNCTIONS

PROJECT_NAME="housing-predictor"
VERSION="22.1.2"
AUTHOR="ADVITEEYA SHRAV"
DESCRIPTION= "THIS IS THE FIRST FSDS NOV. BATCH ML PROJECTS "
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME= "requirements.txt"


def get_requirements_list()->List[str]:

    """
    Description: This function is going to retrun list of requirements mention in requirements to txt.file


    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file

    """
    
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")

setup(
name= PROJECT_NAME,
version= VERSION,
author= AUTHOR,
description= DESCRIPTION,
packages= find_packages(),
install_requirements = get_requirements_list()


)

if __name__=="__main__":
    print(get_requirements_list())
