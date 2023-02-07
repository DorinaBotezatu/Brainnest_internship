"""
File Organizer: Create a script that organizes files into folders based on specific criteria (e.g. file type, date modified).
"""

import os
import shutil

path = "../Organiser"  # The Path of the directory to be sorted
list_with_filenames = os.listdir(path)  # This populates a list with the filenames in the directory

# Traverses every file

for file in list_with_filenames:
    name, file_type = os.path.splitext(file)  # Stores the file_typeension type
    file_type = file_type[1:]

    if file_type == '':  # If it is directory, it forces the nfile_type iteration
        continue
    if os.path.exists(
            path + '/' + file_type):  # If a directory with the name 'file_type' exists, it moves the file to that directory
        shutil.move(path + '/' + file, path + '/' + file_type + '/' + file)
    else:  # If the directory does not exist, it creates a new directory
        os.makedirs(path + '/' + file_type)
        shutil.move(path + '/' + file, path + '/' + file_type + '/' + file)
