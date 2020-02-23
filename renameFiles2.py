import os

path = '/home/andrea/Code/AndreaDiotallevi/p5/twines/Videos'
directories = os.listdir(path)

for directory in directories:
    path = '/home/andrea/Code/AndreaDiotallevi/p5/twines/Videos/' + directory
    files = os.listdir(path)
    for filename in files:
        filename_without_ext = os.path.splitext(filename)[0]
        extension = os.path.splitext(filename)[1]
        new_file_name = directory + filename_without_ext
        new_file_name_with_ext = new_file_name + extension
        os.rename(os.path.join(path, filename),
                  os.path.join(path, new_file_name_with_ext))

