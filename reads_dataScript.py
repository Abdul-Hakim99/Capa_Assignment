#! /usr/bin/python3

import os

cwd = os.getcwd()
items = os.listdir(cwd)

files = [item for item in items if os.path.isfile(os.path.join(cwd, item))]

directories = [item for item in items if os.path.isdir(os.path.join(cwd, item))]

print("files:")
for file in files:
    print(file)

print("\nDirectories:")
for directory in directories:
    print(directory)
