import json     

url = "https://api.cartolafc.globo.com/atletas/pontuados"

with open('pontuados28.json') as json_data:
    d = json.load(json_data)
    print(d)
