#! /usr/bin/python3

import os
import shutil

source_directory = "/home/abdud/Documents"
destination_directory = "/home/abdud/practice/newDir"

file_extension = ".txt"

if not os.path.exists(source_directory):
    print("source directory does not exit.")
else:
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
        print(f"Destination directory '{destination_directory}' created.")

    for filename in os.listdir(source_directory):
        if filename.endswith(file_extension) and os.path.isfile(os.path.join(source_directory, filename)):
            source_file = os.path.join(source_directory, filename)
            destination_file = os.path.join(destination_directory, filename)

            shutil.copy2(source_file, destination_file)
            print(f"copied: {filename}")

            print(f"All {file_extension} files from {source_directory} have been copied to {destination_directory}.") 

