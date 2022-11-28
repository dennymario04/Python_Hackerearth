import json

bio = open("bio.json")

read = json.load(bio)

print(read['nama'])


# test masukan data ke bio.json

bioBaru = {
    "nama" : "Fatwa",
    "umur" : 22,
    "pekerjaan" : "Pejudi Handal" 
}

konversi = json.dumps(bioBaru)

with open('bio.json','w') as f:
    json.dump(bioBaru,f)
