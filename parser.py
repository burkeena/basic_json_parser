
import json
import os

absolute_path = os.path.dirname(__file__)
relative_path = "json/"
full_path = os.path.join(absolute_path, relative_path)

print(absolute_path + "; This is the absolute path")
print(relative_path + "; This is relative path")
print(full_path + "; This is the full path")
print("\n") ## Blank line

json_file = open(relative_path + "file.json") ## Use the relative path, and open the json file

data = json.load(json_file) ## Convert to python dict 

def print_json():
    for i in data['certifications']:
        print(i)

def decode_json():
    print("\n") ## Blank line
    print("This is the decoded JSON example:")
    for cert_names in data['certifications']:
        print(cert_names['name'],cert_names['courses'])

print_json() # Run print_json function
decode_json() # Run decode_json function

json_file.close()
