from typing import Annotated
from pydantic import BaseModel

from fastapi import FastAPI, Depends,Header, HTTPException, Response, Request, Body
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
import jinja2
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.gzip import GZipMiddleware
from sqlalchemy import JSON

#import metadata.testdata
import metadata.src.Catalogs as Catalogs
import metadata.src.Documents as Documents
import metadata.src.InformationRegisters as InformationRegisters
import metadata.src.Forms as Forms
import metadata.src.Commands as Commands
import metadata.src.Templates as Templates
import metadata.src.TabularSections as TabularSections


import uvicorn
import yaml
import os, json

from metadata.testdata import GetTestTree
import metadata.src.Types as Types


ConfigFile = 'metadata.yaml'
data = {"Catalogs": [], "Documents": [], "InformationRegisters": []}
portNumber = '8084'

data = GetTestTree()



app = FastAPI()
app.mount("/metadata", StaticFiles(directory="metadata"), name="metadata")


app.add_middleware(GZipMiddleware)

template = Jinja2Templates(directory="metadata")

def proba():
    return '<div>MAIN PROBA</div>'
@app.get("/", response_class=HTMLResponse) #******************************************************
async def read_root(request: Request):
    #response.headers['Access-Control-Allow-Origin'] = "*"
    #return "<html><body>fdfd</body></html>"
    inveronment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))

    students = 0
    test_name = 0
    max_score = 0
    context = {
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }

    #return templates.TemplateResponse('menu.html', context={"ddd":'ddd', "request":request})
    #dd = template.render(context)
    #url_for = ""
    proba2  = "HELLO PROBAB"
    return template.TemplateResponse('menu.html',context={"ddd":'ddd', "request":request, 'proba' : proba})
    return dd
    #return templates.TemplateResponse('menu.html', context={"ddd":'ddd', "request":request})

    return {"Hello": "World"}

@app.get("/tree/")  #******************************************************
async def read_tree(request: Request):
    res = {'Action' : 'RedrawTree',
           'Tree' : data
           }

    return json.dumps(res)



#
#
#     3 LEVEL    *********************************************
#

@app.get("/{MetadataType}/{MetadataName}/Properties")  #*********************************************
async def read_properties(MetadataType: str, MetadataName : str, request: Request) :
    '''
    Sample: Catalogs/Goods/Properties   - get a propertylist of the Goods catalog.

     tekes an information about one current catalogcatalog
     :param request: CatalogName
     :return: JSON of current Catalog structure
     '''
    PropertyList = {}
    if MetadataType == 'Catalogs' :
        PropertyList = Catalogs.PropertyList
    elif MetadataType == 'Documents':
        PropertyList = Documents.PropertyList
    elif MetadataType == 'InformationRegisters':
        PropertyList = InformationRegisters.PropertyList

    ff = f'/{MetadataType}/{MetadataName}/Properties'
    res = {'requestPath': ff,
           'PropertyList' : PropertyList,
           Types.PROP_VALUE : data[MetadataType][MetadataName]['Properties']
           }
    return json.dumps(res)

class Item(BaseModel):
    Name: str = ''
    Value : str = ''
    Path : str = ''
    PropName : str = ''
    Res : str = ''
    def setRes(self, newRes):
        self.res = newRes

    def setNew(self, Name : str, Value : str, Path : str, PropName : str):
        self.Name = Name
        self.Value = Value
        self.Path = Path
        self.PropName = PropName

#
#
#     5 LEVEL    *********************************************
#

#
@app.post("/{MetadataType}/{MetadataName}/Property/{PropertyName}/ввавав")  #*********************************************
async def edit_one_MetadataName_property_enter3(MetadataType: str, MetadataName: str, PropertyName: str, newValue : Item) :

   # print(newValue)
    edit_one_MetadataName_property(newValue)

    return newValue
    #return JSON.dumps({'res' : True, 'dumps' : ''})

@app.post("/{MetadataType}/{MetadataName}/{ItemType}/{PropertyName}")  #*********************************************
async def edit_one_MetadataName_property_enter33(
        MetadataType: str,
        MetadataName: str,
        ItemType: str,
        PropertyName: str,
        newValue : Item) :

   # print(newValue)
   # edit_one_MetadataName_property(newValue)
    newValue.res = '5'
    return newValue
    #return JSON.dumps({'res' : True, 'dumps' : ''})

def edit_one_MetadataName_property(newValue : Item):

    words = newValue.Path.split('.')
    MetadataType = words[1]
    MetadataName = words[2]

    if not newValue.PropName in data[words[1]][words[2]]['Properties'] :
        data[MetadataType][MetadataName]['Properties'][newValue.PropName] = {}

    data[MetadataType][MetadataName]['Properties'][newValue.PropName]['Value'] = newValue.Value

    newValue.Res = data[MetadataType][MetadataName]['Properties'][newValue.PropName]['Value']

    if newValue.PropName == 'Name' :
        data[MetadataType][newValue.Value] = dict(data[MetadataType][MetadataName])
        data[MetadataType].pop(MetadataName)
        MetadataName = newValue.Value
        newValue.Res = data[MetadataType][MetadataName]['Properties'][newValue.PropName]['Value']

@app.get("/{MetadataType}/{MetadataName}/{ItemType}/{PropertyName}/Properties")  #********************************
async def read_property5(
        MetadataType: str,
        MetadataName: str,
        ItemType: str,
        PropertyName : str  ,
        request: Request  ):
    '''
    sample   http://127.0.0.1:8084/Catalogs/Goods/Attributes/weight/Properties

     tekes an information about one all catalog propertys
     :param request: CatalogName
     :return: JSON of current Catalog structure
     '''
    return read_property5_test(MetadataType, MetadataName, ItemType, PropertyName , request)

def read_property5_test(
            MetadataType: str,
            MetadataName: str,
            ItemType: str,
            PropertyName: str,
            request: Request):

    PropList = {}
    if MetadataType == Types.METADATA_CATALOGS:
        if ItemType == 'Attributes':
            PropList = Types.AttributePropertyList

    elif MetadataType == Types.METADATA_DOCUMENT:
        pass
    elif MetadataType == Types.METADATA_INFOREG:
        pass

    Value = data[MetadataType][MetadataName][ItemType][PropertyName]

    if ItemType == 'Attributes':
        PropList = Types.AttributePropertyList
    elif ItemType == 'Forms':
        PropList = Forms.PropertyList
    elif ItemType == 'Commands':
        PropList = Commands.PropertyList
    elif ItemType == 'Templates':
        PropList = Templates.PropertyList
    elif ItemType == 'TabularSections':
        PropList = TabularSections.PropertyList
        Value = Value['Properties']


    res = {'requestPath': '/Catalogs/{dddd}/Property',
           Types.PROP_VALUE : Value,
           'PropertyList' : PropList
           }
    return json.dumps(res)

@app.get("/{MetadataType}/{MetadataName}/{ItemType}/{PropertyName}/Attributes/{AttributeName}")
async def read_propertyTS7(
        MetadataType: str,
        MetadataName: str,
        ItemType: str,
        PropertyName : str  ,
        AttributeName : str  ,
        request: Request  ):

    PropList = Types.AttributePropertyList
    Value = data[MetadataType][MetadataName][ItemType][PropertyName]['Attributes'][AttributeName]

    res = {'requestPath': '/Catalogs/{dddd}/Property',
           Types.PROP_VALUE: Value,
           'PropertyList': PropList
           }
    return json.dumps(res)







@app.get("/css/")
async def read_items(request: Request):
    ss = '22'
    with open('metadata/menu.css', mode='r') as file:
        try:
            ss = file.read()
        except:
            ss = 'error'
    return ss



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
    ss =  data['Catalogs']['Goods']['Properties']
    sss = data['Catalogs']['Goods']['Attributes']['weight']
    aa = 0

    #newValue = Item()
    #newValue.setNew('Catalogs', '123', 'Catalogs.Goods','Comment')

    #read_one_catalog_action(newValue)
    #print('ddd')

    dd = read_property5_test('Documents','Invoice', 'Attributes', 'Fullname', '')
    print(dd)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
