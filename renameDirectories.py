import os

path = '/home/andrea/Code/AndreaDiotallevi/p5/twines/Videos'
directories = os.listdir(path)
n = 0

for directory in directories:
    if "(" not in directory:
        directory_new_name = "0"
    else:
        firstIndex = directory.find('(')
        secondIndex = directory.find(')')
        directory_new_name = directory[(firstIndex+1):secondIndex]
    os.rename(os.path.join(path, directory),
              os.path.join(path, directory_new_name))
