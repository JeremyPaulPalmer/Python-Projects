import os
import fnmatch


fPath = 'C:\\python_projects\\'

folder_list = os.listdir(fPath)

desired = '*.txt'
matchingText = fnmatch.filter(folder_list, desired)


for i in matchingText:
    abPath = os.path.join(fPath, i)
    print(abPath + ' ' + str(os.path.getmtime(abPath)))

