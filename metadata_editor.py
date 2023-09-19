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
portNumber = '8082'

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
    return template.TemplateResponse('menu.html',
                                     context={
                                         "ddd":'ddd',
                                         "request":request,
                                         'proba' : proba
                                     }
                                     )

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

class IgnoredType:
    pass

class EditItem(BaseModel):
    #Name: str = ''
    Value: str = ''
    ValueType: str = ''
    ValueAsBool: bool = False
    ValueAsNumber: int = 0
    #PropertyPath : str = ''
    PropertyName : str = ''
    #new_id : str = ''
    Res : str = ''
    def setRes(self, newRes):
        self.res = newRes

    def setNew(self, Name : str, Value : str, PropertyPath : str, PropertyName : str):
        self.Name = Name
        self.Value = Value
        self.PropertyPath = PropertyPath
        self.PropertyName = PropertyName

#
#
#     5 LEVEL    *********************************************
#

#
@app.post("/{MetadataType}/{MetadataName}/{ItemType}/{PropertyName}")  #*********************************************
async def edit_one_MetadataName_property_enter_3_level(
        MetadataType: str,
        MetadataName: str,
        ItemType : str,
        PropertyName: str,
        newValue : EditItem) :

    # sample Catalogs.Goods.Property.Synonim
   new_struct = {
       'MetadataType' : MetadataType,
       'MetadataName' : MetadataName,
       'ItemType' : ItemType,
       'PropertyName' : PropertyName,
       'LevelType': '',
       'LevelPropName': ''
    }

   edit_one_MetadataName_property(newValue, new_struct)

   return newValue
@app.post("/{MetadataType}/{MetadataName}/{ItemType}/{PropertyName}/{LevelType}/{LevelPropName}")  # *********************************************
async def edit_one_MetadataName_property_enter_5_level(
        MetadataType: str,
        MetadataName: str,
        ItemType: str,
        PropertyName: str,
        LevelType: str,
        LevelPropName: str,
        newValue: EditItem):
    # sample Catalogs.Goods.Property.Synonim
    new_struct = {
        'MetadataType': MetadataType,
        'MetadataName': MetadataName,
        'ItemType': ItemType,
        'PropertyName': PropertyName,
        'LevelType': LevelType,
        'LevelPropName': LevelPropName
    }

    edit_one_MetadataName_property(newValue, new_struct)

    return newValue


def edit_one_MetadataName_property(newValue : EditItem, new_struct : dict):


    MetadataType = new_struct['MetadataType']
    MetadataName = new_struct['MetadataName']
    ItemType = new_struct['ItemType']   #Attributes/Properties/TabularSections/Forms
    PropertyName = new_struct['PropertyName']
    LevelType = new_struct['LevelType']
    LevelPropName = new_struct['LevelPropName']

    newValueRes = newValue.Value
    if newValue.ValueType == 'checkbox' :
        newValueRes = newValue.ValueAsBool
    if newValue.ValueType == 'number' :
        newValueRes = newValue.ValueAsNumber

    if ItemType == 'Properties' : #3-th level

        if not newValue.PropertyName in data[MetadataType][MetadataName][ItemType]:
            data[MetadataType][MetadataName][ItemType][newValue.PropertyName] = {}

        data[MetadataType][MetadataName][ItemType][newValue.PropertyName]['Value'] = newValueRes
        newValue.Res = data[MetadataType][MetadataName][ItemType][newValue.PropertyName]['Value']

        if newValue.PropertyName == 'Name':
            data[MetadataType][newValueRes] = dict(data[MetadataType][MetadataName])
            data[MetadataType].pop(MetadataName)
            MetadataName = newValueRes
            newValue.Res = data[MetadataType][MetadataName][ItemType][newValue.PropertyName]['Value']





    else:         # 5-th level

        if new_struct['LevelType'] == '':
            if not PropertyName in data[MetadataType][MetadataName][ItemType]:
                data[MetadataType][MetadataName][ItemType][PropertyName] = {}

            if not newValue.PropertyName in data[MetadataType][MetadataName][ItemType][PropertyName]:
                data[MetadataType][MetadataName][ItemType][PropertyName][newValue.PropertyName] = {}

            data[MetadataType][MetadataName][ItemType][PropertyName][newValue.PropertyName]['Value'] = newValueRes
            newValue.Res = data[MetadataType][MetadataName][ItemType][PropertyName][newValue.PropertyName]['Value']

            if newValue.PropertyName == 'Name':
                newPropertyName = newValueRes
                data[MetadataType][MetadataName][ItemType][newPropertyName] = \
                    dict(data[MetadataType][MetadataName][ItemType][PropertyName])
                data[MetadataType][MetadataName][ItemType].pop(PropertyName)
                PropertyName = newPropertyName
                newValue.Res = data[MetadataType][MetadataName][ItemType][PropertyName][newValue.PropertyName]['Value']





        elif new_struct['LevelType'] == 'Properties':
            # tabular section property
            if  not newValue.PropertyName in data[MetadataType][MetadataName][ItemType][PropertyName][LevelType]:
                data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][newValue.PropertyName] = {}

            data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][newValue.PropertyName]['Value']  = newValueRes
            newValue.Res = data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][newValue.PropertyName]['Value']

            if newValue.PropertyName == 'Name':
                newPropertyName = newValueRes
                data[MetadataType][MetadataName][ItemType][newPropertyName] = dict(
                    data[MetadataType][MetadataName][ItemType][PropertyName])
                data[MetadataType][MetadataName][ItemType].pop(PropertyName)
                PropertyName = newPropertyName
                newValue.Res = data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][newValue.PropertyName]['Value']


        else:
            # tabular section attributes

            if not LevelPropName  in data[MetadataType][MetadataName][ItemType][PropertyName][LevelType]:
                data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][LevelPropName] = {}

            if not newValue.PropertyName in data[MetadataType][MetadataName][ItemType][PropertyName][LevelType]:
                data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][LevelPropName][newValue.PropertyName] = {}

            data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][LevelPropName][newValue.PropertyName]['Value'] = \
                newValueRes
            newValue.Res = data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][LevelPropName][newValue.PropertyName]['Value']

            if newValue.PropertyName == 'Name':
                newPropertyName = newValueRes
                data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][newPropertyName] = dict(
                    data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][LevelPropName])
                data[MetadataType][MetadataName][ItemType][PropertyName][LevelType].pop(LevelPropName)
                LevelPropName = newPropertyName
                newValue.Res = data[MetadataType][MetadataName][ItemType][PropertyName][LevelType][LevelPropName][newValue.PropertyName]['Value']



    dd = 0


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

    new_struct = {
        'MetadataType': 'Catalogs',
        'MetadataName': 'Goods',
        'ItemType': 'Attributes',
        'PropertyName': 'Fullname',
        'LevelType': '',
        'LevelPropName': ''
    }

    new_struct = {
        'MetadataType': 'Catalogs',
        'MetadataName': 'Goods',
        'ItemType': 'TabularSections',
        'PropertyName': 'Goods',
        'LevelType': 'Attributes',
        'LevelPropName': 'Count'
    }

    newVal = EditItem()
    #dd = {Name: 'sdsdsd', Value: 'sss', Path: 'mytree1.Catalogs.Goods.Attributes.weight', PropertyName: 'Type', res: ''}
    #newVal.Name = ''
    newVal.Value = 'sss'
    newVal.ValueType = 'text'
    newVal.ValueAsBool = False
    newVal.ValueAsNumber = 0

   # newVal.PropertyPath = 'mytree1.Catalogs.Goods.Properties.Comment'
    newVal.PropertyName = 'Name'
    edit_one_MetadataName_property(newVal, new_struct)


    dd = [['a'], ['b']]
    print(dd)

    dd = read_property5_test('Documents','Invoice', 'Attributes', 'Fullname', '')
    print(dd)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
