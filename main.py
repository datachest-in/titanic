########################################
# Author: Abhisek Ashirbad Sethy
# Copyright (c) 2020, datachest.in
# License: GPLv3
# Web: https://www.datachest.in
########################################

# Import modules
import os

from utils.data_analysis import DataAnalyser
from utils.file_info import check_for_files, get_data_file_info
from utils.read_properties import ReadProperties as rp


config = rp(filepath="main_config.properties")
config.read_properties()

# Defining data source
# Defining root directory for the project.
ROOT_DIR = os.getcwd()
print("\nRoot Directory: ",ROOT_DIR)
# Defining data source directory for the project.
DATA_DIR = os.path.join(ROOT_DIR, config.data_dir)
print("\nData Source Directory: ",DATA_DIR)

# Data file extraction
DATA_FILE = os.path.join(DATA_DIR, config.data_file)

# Main code
if __name__ == '__main__':
    check_for_files(DATA_DIR)
    get_data_file_info(DATA_FILE)
    # Data analysis
    data_analyser = DataAnalyser(DATA_FILE)
    data_analyser.start_analysis()


