from typing import Annotated
from fastapi import FastAPI, Depends,Header, HTTPException, Response
from fastapi.routing import APIRoute

import uvicorn
import yaml
import os, json

ConfigFile = 'metadata.yaml'
data = {"Catalogs": [], "Documents": [], "InformationRegisters": []}

newCatalog = {
    'Name': 'Goods',
    'Description': 'Goods',
    'Attributes': [],
    'TabularSections': [],
    'Templates': [],
    'Commands': []
}
newAttribute = {
    "Name" : "weight",
    "type" : 'Number',
    "length" : 15,
    "dim" : 0,
    'format' : "",
    'indexed' : False
}
newCatalog['Attributes'].append(newAttribute)
newAttribute = {
    "Name" : "Fullname",
    "type" : 'String',
    "length" : 50,
    "dim" : 0,
    'format' : "",
    'indexed' : False
}
newCatalog['Attributes'].append(newAttribute)

data['Catalogs'].append(newCatalog)

newCatalog = {
    'Name': 'Customers',
    'Description': 'Company customers',
    'Attributes': [],
    'TabularSections': [],
    'Templates': [],
    'Commands': []
}
data['Catalogs'].append(newCatalog)



app = FastAPI()


@app.get("/")
async def read_root(response: Response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    #return {"Hello": "World"}
    return data

@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]


class CatalogItem:

    Name : str = '',
    Description : str = ''
    Attributes : list = [],
    TabularSections: list = [],
    Templates: list = [],
    Commands: list = []

    def __init__(self, Name):
        self.Name = Name

    def loadJSON(self):

        pass

    def dumpStructure(self):
        struct = {
            'Name' : self.Name,
            'Description': self.Description,
            'Attributes': self.Attributes,
            'TabularSections': self.TabularSections,
            'Templates': self.Templates,
            'Commands': self.Commands
        }

        return struct

    def dumpJSON(self):
        struct = self.dumpStructure(self)

        return ''

def readConfig():

    if not os.path.exists(ConfigFile):
        yaml_output = yaml.dump(data, sort_keys=False)

        with open(ConfigFile, mode="w") as file:
            file.write(yaml_output)

    #print(yaml_output)

    res = 1
    with open(ConfigFile, mode="r") as file:
        res = yaml.load(file, Loader=yaml.FullLoader)

    print('RESULT')
    print(res)

    #yaml_output = yaml.dump(data, sort_keys=False)

def print_hi(name):

    readConfig()


       #uvicorn.run(app, host="0.0.0.0", port=8000)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
