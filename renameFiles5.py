import os
import shutil

path = '/home/andrea/Code/AndreaDiotallevi/p5/twines/Videos'
directories = sorted(os.listdir(path))
n = 0

for directory in directories:    
    path = '/home/andrea/Code/AndreaDiotallevi/p5/twines/Videos/' + directory
    files = sorted(os.listdir(path))    
    for filename in files:
        filename_without_ext = os.path.splitext(filename)[0]
        extension = os.path.splitext(filename)[1]
        new_file_name = str(n).zfill(7)
        new_file_name_with_ext = new_file_name + extension
        os.rename(os.path.join(path, filename),
                  os.path.join(path, new_file_name_with_ext))       
        print("1 ", new_file_name)
        n+=1        

for directory in directories:
    path = '/home/andrea/Code/AndreaDiotallevi/p5/twines/Videos/' + directory
    files = sorted(os.listdir(path))
    for filename in files:
        newPath = shutil.move(path + "/" + filename, '/home/andrea/Code/AndreaDiotallevi/p5/output/')
        print(filename)

