import os

path = '/home/andrea/Downloads/TwinesVersion2'
files = os.listdir(path)

for file in files:
    if '(' in file:
        os.remove(path+"/"+file)
