import os
import shutil

path = input("please enter path")
list_files = os.listdir(path)
for file in list_files:
    name, ext = os.path.splittext(files)
    ext = ext[1:] - py
    if(ext == ""):
        continue
    if(os.path.exists(path+"/"+ext)):
        shutil.move(path+"/"+file, path+"/"+ext+"/"+file)
    else:
        os.makedirs(path+"/"+ext)
        shutil.move(path+"/"+file, path+"/"+ext+"/"+file)
