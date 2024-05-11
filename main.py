########################################
# Author: Abhisek Ashirbad Sethy
# Copyright (c) 2020, datachest.in
# License: GPLv3
# Web: https://www.datachest.in
########################################

# Import modules
import os
from jproperties import Properties

from utils.file_info import check_for_files


# Reading .properties file.
config = Properties()
with open('main_config.properties', 'rb') as cfg_file:
    config.load(cfg_file)
# Get all config values from  .properties file.
data_dir = config.get('data_dir').data
# Closing the config file.
cfg_file.close()

# Testing the values from the .properties file.
# print(data_dir)


# Defining data source
# Defining root directory for the project.
ROOT_DIR = os.getcwd()
print("\nRoot Directory: ",ROOT_DIR)
# Defining data source directory for the project.
DATA_DIR = os.path.join(ROOT_DIR, data_dir)
print("\nData Source Directory: ",DATA_DIR)


# Main code
if __name__ == '__main__':
    check_for_files(DATA_DIR)


