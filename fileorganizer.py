import shutil
import os
import shutil

path="C:/Users/palaa/OneDrive/Desktop/whitehat/python/c99"
listoffiles=os.listdir(path)

for file in listoffiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]

    if ext=="":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)