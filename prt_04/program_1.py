import os

_path_ = input("Enter Path : ")

if _path_ :
    for folder in os.scandir(_path_) :
        if folder.is_dir() :
            print(folder.path)
else :
    _path_ = os.getcwd()
    print("Path : ",_path_)
    for folder in os.scandir(_path_) :
        if folder.is_dir() :
            print(folder.path)
