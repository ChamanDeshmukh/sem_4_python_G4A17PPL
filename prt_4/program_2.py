import os

_path_ = input("Enter Path : ")

if _path_ :
    for curr,folder,file in os.walk(_path_) :
        print("Current Dir : ",curr)
        print("Folders : ",folder)
        print("Files : ",file)
else :
    _path_ = os.getcwd()
    print("Path : ",_path_)
    for curr,folder,file in os.walk(_path_) :
        print("Current Dir : ",curr)
        print("Folders : ",folder)
        print("Files : ",file)
