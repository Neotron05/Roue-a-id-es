import json

#read the file
jsonFile = open('things.json','r')
data = jsonFile.read()

#Parse the json
objects = json.loads(data)

print(objects["idees"][0])
