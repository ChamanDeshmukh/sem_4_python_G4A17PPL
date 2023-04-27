import os
from datetime import datetime

_path_ = input("Enter Path : ")

if _path_ :
    print("Mode : ",os.stat(_path_).st_mode)
    print("Owner : ",os.stat(_path_).st_dev)
    print("Created : ",datetime.fromtimestamp(os.stat(_path_).st_ctime))
    print("Last Modified : ",datetime.fromtimestamp(os.stat(_path_).st_mtime))
    print("Last Accessed : ",datetime.fromtimestamp(os.stat(_path_).st_atime))
else :
    _path_ = os.getcwd() 
    print("Path : ",_path_)
    print("Mode : ",os.stat(_path_).st_mode)
    print("Owner : ",os.stat(_path_).st_dev)
    print("Created : ",datetime.fromtimestamp(os.stat(_path_).st_ctime))
    print("Last Modified : ",datetime.fromtimestamp(os.stat(_path_).st_mtime))
    print("Last Accessed : ",datetime.fromtimestamp(os.stat(_path_).st_atime))
