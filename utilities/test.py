import json

myJsonfile = open('./utilities/test_Data.json', 'r')
jsonData = myJsonfile.read()

# Parse the data
obj = json.loads(jsonData)
print(str(obj['NCFirst_Name']))