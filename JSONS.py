import json


def read(url):
    # read the file
    jsonFile = open(url, 'r')
    data = jsonFile.read()
    jsonFile.close()
    # Parse the json
    objects = json.loads(data)

    return objects


''' probleme d'encodage

def add(url, opt, obj):
    jsonFile = open(url, 'w')
    str_to_add = "{\n"
    print("Entrez le nom")
    nom = str(input())
    str_to_add += '"nom": "' + nom + '"'
    if opt == 1:
        str_to_add += ',\n'
        print("Entrez la description")
        desc = str(input())
        str_to_add += '"description": "' + desc + '"'
        str_to_add += '\n}'
        obj["idees"].append(str_to_add)
    else:
        str_to_add += '\n}'
        obj["langages"].append(str_to_add)
    obj.encode()
    json.dump(obj,jsonFile)
'''


def printJson(url):
    print(read(url))
