########################################
# Author: Abhisek Ashirbad Sethy
# Copyright (c) 2020, datachest.in
# License: GPLv3
# Web: https://www.datachest.in
########################################

# Import modules
from jproperties import Properties

class  ReadProperties():

    def __init__(self, filepath=None):
        self.filepath = filepath
 
    def read_properties(self): 
        try:
            if self.filepath:
                # Reading .properties file.
                config = Properties()
                with open(self.filepath, 'rb') as cfg_file:
                    config.load(cfg_file)

                # Get all config values from  .properties file.
                self.data_dir = config.get('data_dir').data
                self.data_file = config.get('data_file').data
        except Exception as e:
            # print(FileNotFoundError(e))
            raise FileNotFoundError(e)



