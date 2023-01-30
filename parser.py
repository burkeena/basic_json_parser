
import json
import os

absolute_path = os.path.dirname(__file__)
relative_path = "json/"
full_path = os.path.join(absolute_path, relative_path)

print(absolute_path + "; This is the absolute path")
print(relative_path + "; This is relative path")
print(full_path + "; This is the full path")

json_file = open(relative_path + "file.json") ## Use the relative path, and open the json file

data = json.load(json_file) ## 

for i in data['certifications']:
    print(i)

json_file.close()