#! /usr/bin/python3

with open('input.txt', 'r') as input_file:
    file_content = input_file.read()

with open('output.txt', 'w') as output_file:
    output_file.write(file_content)

    print("file copied successfully")
