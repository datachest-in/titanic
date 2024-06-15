########################################
# Author: Abhisek Ashirbad Sethy
# Copyright (c) 2020, datachest.in
# License: GPLv3
# Web: https://www.datachest.in
########################################

# Import modules
import os

from datetime import datetime as dt
from tzlocal import get_localzone


def check_for_files(directory):
    """
    Check for files in the directory.

    Args:
    - directory (str): Path to the directory.
    """
    try:
        if directory != None and os.path.exists(directory): # Checking if the data source directory exists or not. If it does, then proceed to next step else print error message.
            filelist = os.listdir(directory) # List all files in data source directory.
            print("\nFiles Info: ")
            print("___________")
            print("Total file count: ", len(filelist))
            list_file_extensions_with_counts(directory=directory)
            list_files_sorted_by_extension(directory=directory)            
    except Exception as err_msg: # Checking if any error has occurred. If yes, then proceed to next step else print error message.
        print("\nError Message: ", err_msg) # Printing the error message.



def list_file_extensions_with_counts(directory):
    """
    List all file extensions present in a directory along with the number of files for each extension.

    Args:
    - directory (str): Path to the directory.
    """
    # Initialize a dictionary to store file extension counts
    extension_counts = {}
    # Iterate through the files in the directory
    for filename in os.listdir(directory):
        # Split the filename into its base and extension
        _, ext = os.path.splitext(filename)
        # Increment the count for this extension in the dictionary
        extension_counts[ext] = extension_counts.get(ext, 0) + 1
    # Sort the file extensions alphabetically
    sorted_extensions = sorted(extension_counts.items(), key=lambda x: x[0])
    # Print the number of files for each extension
    print("\nFile types and their counts:")
    for ext, count in sorted_extensions:
        print(f"*{ext} : {count} file(s)")


def list_files_sorted_by_extension(directory):
    """
    List all files in a directory sorted alphabetically by their extensions.
    
    Args:
    - directory (str): Path to the directory.
    """
    # Initialize a list to store file names 
    files = []
    # Iterate through the files in the directory
    for filename in os.listdir(directory):
        # Append the filename to the list
        files.append(filename)
    # Sort the files alphabetically by their extensions
    files.sort(key=lambda x: (os.path.splitext(x)[1], x))
    # Print the sorted files
    print("\nFiles available in datasource directory:")
    print("________________________________________")
    for file in files:
        print(file)


def get_data_file_info(filename):
    """
    Get the datafile information.
    
    Args:
    - filename (str): Path to the datafile.
    """
    # Datafile Information
    print("\nData file to be analysed: ", filename)
    filetype = os.path.splitext(filename)[1]
    print("File type: ", filetype)
    filesize = os.path.getsize(filename)
    print("File size (bytes): ", filesize)
    file_modified_time = get_last_modified_time(filename)
    print("Time of last modification (UTC):", file_modified_time, sep="\t")


def get_last_modified_time(file_path):
    """
    Get the last modified time of a file in the local timezone.
    
    Args:
    - file_path (str): Path to the file.
    
    Returns:
    - str: Last modified time of the file in the local timezone, formatted as a string.
    """
    # Get the last modified time of the file in seconds since the epoch
    last_modified_time = os.path.getmtime(file_path)
    # Get the local timezone
    local_timezone = get_localzone()
    # Convert the time to a datetime object and localize it to the local timezone
    localized_last_modified_datetime = dt.fromtimestamp(last_modified_time).replace(tzinfo=local_timezone)
    # Format the localized datetime as a string
    formatted_time = localized_last_modified_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    return formatted_time
