# move all .jpg files from a folder to a new folder

import os
import shutil
source_folder = r"D:\from" # use r"path" if ur path contains \f, \n or \t
destination_folder = r"D:\to"

files = os.listdir(source_folder) # lists all files in the folder
for file in files:
    if file.endswith(".jpg"):
        source = os.path.join(source_folder, file) # creates a full path
        destination = os.path.join(destination_folder, file) # full path for destination 
        shutil.move(source, destination)
        print(f"Moved: {file}")


