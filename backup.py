from msilib.schema import Directory
import os
import shutil 

source="C:/Users/palaa/OneDrive/Desktop/whitehat/python/c99/txt"
destination="C:/Users/palaa/OneDrive/Desktop/whitehat/python/c99/newfolder"

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)