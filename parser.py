import json
import os

## Get paths and combine to create full path
absolute_path = os.path.dirname(__file__)
relative_path = "json/"
file_name = "file.json"
full_path = os.path.join(absolute_path, relative_path, file_name)
print("\n") ## Blank line

json_class = input("Enter JSON Class to Extract:")
print("The JSON class you selected is: " + json_class)
print("\n") ## Blank line

## Column names 
column_1 = input("What is column 1's name?:")
column_2 = input("What is column 2's name?:")

print(absolute_path + "; This is the absolute path")
print(relative_path + "; This is relative path")
print(full_path + "; This is the full path")
print("\n") ## Blank line

json_file = open(full_path) ## Use the full path, and open the json file

data = json.load(json_file) ## Convert to python dict 

def print_json(): ## Print dictionary function
    print("\n") ## Blank line
    print("This is the loaded JSON Sample:")
    for i in data[json_class]:
        print(i)

def decode_json(): ## Decode dictionary function
    print("\n") ## Blank line
    print("This is the decoded JSON example:")
    for cert_names in data[json_class]:
        print(cert_names[column_1],cert_names[column_2])


print_json() # Run print_json function
decode_json() # Run decode_json function


json_file.close()
