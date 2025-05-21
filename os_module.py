#os module provides a way of using operating system dependent functionality like reading or writing to the file system


import os
#os.getcwd() returns the current working directory
current_directory=os.getcwd()
print(current_directory)

#os.listdir() returns a list of the files and directories in the specified directory
files_and_directories=os.listdir(current_directory)
print(files_and_directories)

#os.mkdir() creates a new directory
new_directory="new_directory"
os.mkdir(new_directory)
print(f"Directory '{new_directory}' created")
#os.rmdir() removes a directory
os.rmdir(new_directory)
print(f"Directory '{new_directory}' removed")

#os.path.join() joins one or more path components intelligently
path=os.path.join(current_directory,"new_directory")
print(path)

#os.path.exists() checks if a path exists
if os.path.exists(path):
    print(f"Path '{path}' exists")
else:
    print(f"Path '{path}' does not exist")

#os.path.isfile() checks if a path is a file
if os.path.isfile(path):
    print(f"Path '{path}' is a file")
else:
    print(f"Path '{path}' is not a file")

#os.path.isdir() checks if a path is a directory
if os.path.isdir(path):
    print(f"Path '{path}' is a directory")
else:
    print(f"Path '{path}' is not a directory")

#os.path.abspath() returns the absolute path of a file or directory
absolute_path=os.path.abspath("new_directory")
print(absolute_path)

#os.path.basename() returns the base name of a file or directory
base_name=os.path.basename(path)
print(base_name)

#os.path.dirname() returns the directory name of a file or directory
directory_name=os.path.dirname(path)
print(directory_name)
