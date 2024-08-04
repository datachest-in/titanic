########################################
# Author: Abhisek Ashirbad Sethy
# Copyright (c) 2020, datachest.in
# License: GPLv3
# Web: https://www.datachest.in
########################################

# Import modules
import pandas as pd

class DataAnalyser:

    def __init__(self, datafile):
        self.datafile = datafile

    def preprocess(self):
        print("\n=================================")
        print("#  Data Analysis in progress ...")
        print("=================================\n")
        # Creating dataframe from the datafile.
        df = pd.read_csv(self.datafile)
        print(df)
        # Extracting the column names from the data file.
        columns=df.columns.to_list()
        print("\nColumn Names: ", ", ".join(columns))
        cols=df.shape[1] # number of columns in the data file.
        print("\nNumber of Columns: ", cols)
        rows=df.shape[0] # number of rows in the data file.
        print("Number of Rows: ", rows)
