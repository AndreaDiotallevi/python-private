import os

path = '/home/andrea/Code/AndreaDiotallevi/p5/twines/Videos/new'
files = os.listdir(path)

n = 0

for filename in files:
    n += 1
    filename_without_ext = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    new_file_name = str(n).zfill(3)
    new_file_name_with_ext = new_file_name + extension
    os.rename(os.path.join(path, filename),
              os.path.join(path, new_file_name_with_ext))
