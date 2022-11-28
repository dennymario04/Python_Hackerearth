import json

file = open("bio.json")

load = json.load(file)

print(load["nama"])

