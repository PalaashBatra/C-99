import os

os.system("date")
os.mkdir("newfolder")
path="C:/Users/palaa/OneDrive/Desktop/whitehat/python/c99/test.py"
isexist=os.path.exists(path)
print(isexist)
root_ext=os.path.splitext(path)
print(root_ext)
a=os.listdir()
b=os.getcwd()
print(a)
print(b)