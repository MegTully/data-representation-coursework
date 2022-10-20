from ast import Pass
import requests
import json

Url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en/JSON-stat/2.0/en"

def getAll():
    response = requests.get(Url)
    return response.json()

if __name__ == "__main__" :
    with open("cso.json", "wt") as fp: 
        print(json.dumps(getAll()), file = fp)

