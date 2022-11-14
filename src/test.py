import json
with open('map.dat') as infile:
    x = json.load(infile)
print(x)