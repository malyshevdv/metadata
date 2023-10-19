'''
main module of medatata editor
to work with FastApi
clone in into youe project and fun FastApi with port-number
Port in this module and in menu.html musk be same.

get a menu to work with metadata-editoe interface.
lets you discribe metadata structure of youe project without codding
after finnishing - you can generate PY models files for SQLAlchimy automaticaly
'''

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
import logging

#import metadata.testdata
import metadata.src.Types as Types
import metadata.src.Metadata as Metadata


import uvicorn
import yaml
import os, json

from metadata.testdata import GetTestTree
import metadata.src.Types as Types


ConfigFile = 'metadata.yaml'
#data = {"Catalogs": [], "Documents": [], "InformationRegisters": []}
portNumber = '8082'

myMetadata = GetTestTree()



myLogging = logging.getLogger('Editing')
myLogging.setLevel(logging.INFO)

myFileHandler = logging.FileHandler('metadata\\logs\\mylog.txt', encoding='utf-8')
myFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
myFileHandler.setFormatter(myFormatter)
myFileHandler.setLevel(logging.INFO)
myLogging.addHandler(myFileHandler)

app = FastAPI()
app.mount("/metadata", StaticFiles(directory="metadata"), name="metadata")


app.add_middleware(GZipMiddleware)

template = Jinja2Templates(directory="metadata")

@app.get("/", tags=['settings'], response_class=HTMLResponse) #******************************************************
async def read_root(request: Request):
    '''
      get a menu to work with metadata-editoe interface.
      lets you discribe metadata structure of youe project without codding
      after finnishing - you can generate PY models files for SQLAlchimy automaticaly
      '''

    myLogging.error('read tree')

    students = 0
    test_name = 0
    max_score = 0
    context = {
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }

    proba2  = "HELLO PROBAB"
    return template.TemplateResponse('menu.html',
                                     context={
                                         "ddd":'ddd',
                                         "request":request
                                     }
                                     )

@app.get("/tree/", tags=['settings'])  #******************************************************
async def read_tree(request: Request):
    '''
      get a complete tree from backed to frontend
    '''

    data = myMetadata.GetTreeStructure()

    res = {'Action' : 'RedrawTree',
           'Tree' : data
           }

    return json.dumps(res)

class CreateModel2(BaseModel):
    '''
    structur model for PUT-request CreateItem
    '''
    Action: str = 'new'
    Name : str = ''
    Path : str = ''
    Result :bool = False



def getNextName(Path : str):
    '''
     get a new possible name of object, described in Path
     for Catalogs -> NewCatalog2
     for Documents -> NewDocument5
    '''
    data = {}
    words = Path.split('.')
    TypeName = words[-1]
    NewName = Types.MetadataTypes[TypeName].get('NewItemName', 'NewItem')
    CurrentLength = len(data[words[1]])
    match len(words):
        case 2 :
            CurrentLength = len(data[words[1]])
        case 3 :
            CurrentLength = len(data[words[1]][words[2]])
        case 4 :
            CurrentLength = len(data[words[1]][words[2]][words[3]])
        case 5 :
            CurrentLength = len(data[words[1]][words[2]][words[3]][words[4]])
        case 6 :
            CurrentLength = len(data[words[1]][words[2]][words[3]][words[4]][words[5]])
        case 7 :
            CurrentLength = len(data[words[1]][words[2]][words[3]][words[4]][words[5]][words[6]])
        case 8 :
            CurrentLength = len(data[words[1]][words[2]][words[3]][words[4]][words[5]][words[6]][words[7]])

    #CurrentLength = CurrentLength+1
    NewName = f"{NewName}{CurrentLength+1}"

    return NewName


# PUT  - CREATE NEW OBJECT

@app.put("/CreateItem/", tags=['Items'])  #*********************************************
async def create_new_item(Instruction : CreateModel2):
    '''
      PUT handler for /CreateItem/
      describe Path of new onject inside of Instruction.Path
      like a mytree1.InformationRegisters.Attributes
      and as resunt new Attribute will be added
     '''

    ss = 0
    Instruction.Name = 'NewItem1'
    Instruction.Result = True

    #if MetadataType == 'Catalogs' :
    create_new_item_simple(Instruction)

    return Instruction

def create_new_item_simple(Instruction : CreateModel2):
    '''
     body of main function for append new clear object
    '''
    data = {}
    words = Instruction.Path.split('.')
    Instruction.Name = getNextName(Instruction.Path)

    NewItem = {}

    ItemType = words[-1]

    match ItemType:
        case 'Catalogs':
            NewItem = Catalogs.CreateNewItem(Instruction.Name)
        case 'Documents':
            NewItem = Documents.CreateNewItem(Instruction.Name)
        case 'InformationRegisters':
            NewItem = InformationRegisters.CreateNewItem(Instruction.Name)

        case 'TabularSections':
            NewItem = Types.CreateNewTabular(Instruction.Name)

        case 'Attributes':
            NewItem = Types.CreateNewAttribute_String(Instruction.Name)
        case 'Dimentions':
            NewItem = Types.CreateNewAttribute_String(Instruction.Name)
        case 'Resourses':
            NewItem = Types.CreateNewAttribute_String(Instruction.Name)
        case 'Forms':
            NewItem = Types.CreateNewForm(Instruction.Name)
        case 'Commands':
            NewItem = Types.CreateNewCommand(Instruction.Name)

    match len(words):
        case 2:
            data[words[1]][Instruction.Name] = NewItem
        case 3:
            data[words[1]][words[2]][Instruction.Name] = NewItem
        case 4:
            data[words[1]][words[2]][words[3]][Instruction.Name] = NewItem
        case 5:
            data[words[1]][words[2]][words[3]][words[4]][Instruction.Name] = NewItem
        case 6:
            data[words[1]][words[2]][words[3]][words[4]][words[5]][Instruction.Name] = NewItem
        case 7:
            data[words[1]][words[2]][words[3]][words[4]][words[5]][words[6]][Instruction.Name] = NewItem

#
#
#     3 LEVEL    *********************************************
#

@app.get("/{MetadataType}/{MetadataName}/Properties", tags=['Properties'])  #*********************************************
async def read_properties(MetadataType: str, MetadataName : str, request: Request) :
    '''
    tekes an information about one current catalogcatalog
    Sample: Catalogs/Goods/Properties   - get a propertylist of the Goods catalog.
     :param request: CatalogName
     :return: JSON of current Catalog structure
     '''
    data = {}
    PropertyList = {}
    if MetadataType == 'Catalogs' :
        PropertyList = Types.CatalogPropertyList
    elif MetadataType == 'Documents':
        PropertyList = Types.DocumentPropertyList
    elif MetadataType == 'InformationRegisters':
        PropertyList = Types.InformationRegisterPropertyList

    ff = f'/{MetadataType}/{MetadataName}/Properties'
    res = {'requestPath': ff,
           'PropertyList' : PropertyList,
           Types.PROP_VALUE : data[MetadataType][MetadataName]['Properties']
           }
    return json.dumps(res)

class EditItem(BaseModel):
    '''
      data-structure for transfere new values of edited properties from front-end to backend
     '''

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
@app.post("/{MetadataType}/{MetadataName}/{ItemType}/{PropertyName}", tags=['Properties'])  #*********************************************
async def edit_one_MetadataName_property_enter_3_level(
        MetadataType: str,
        MetadataName: str,
        ItemType : str,
        PropertyName: str,
        newValue : EditItem) :
    '''
      POST request handler to save edited value of object property
      sample InformationRegisters/Prices/Attributes/Customer
      sample InformationRegisters/Prices/Properties/Name
      sample Catalogs.Goods.Property.Synonim
     '''


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
@app.post("/{MetadataType}/{MetadataName}/{ItemType}/{PropertyName}/{LevelType}/{LevelPropName}", tags=['Properties'])  # *********************************************
async def edit_one_MetadataName_property_enter_5_level(
        MetadataType: str,
        MetadataName: str,
        ItemType: str,
        PropertyName: str,
        LevelType: str,
        LevelPropName: str,
        newValue: EditItem):
    '''
          POST request handler to save edited value of object property for 6-th level sach as Tabular section
          sample Documents/Prices/TabularSection/Attributes/Count
          sample Catalogs/Goods/TabularSection/Properties/Name/
    '''
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
    '''
    Basic module for editing values of property
    also it makes Rename function of metadata nopredefined elements
    '''

    data = {}

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


@app.get("/{MetadataType}/{MetadataName}/{ItemType}/{PropertyName}/Properties", tags=['Properties'])  #********************************
async def read_property5(
        MetadataType: str,
        MetadataName: str,
        ItemType: str,
        PropertyName : str  ,
        request: Request  ):
    '''
     tekes an information about one all PropertyName properties
     :param request: CatalogName
     :return: JSON of current Catalog structure
     sample   http://127.0.0.1:8084/Catalogs/Goods/Attributes/weight/Properties
     '''
    return read_property5_test(MetadataType, MetadataName, ItemType, PropertyName , request)

def read_property5_test(
            MetadataType: str,
            MetadataName: str,
            ItemType: str,
            PropertyName: str,
            request: Request):
    '''
      main procedure to returm propertu for upper described function
      that return property list
    '''
    PropList = {}
    if MetadataType == Types.METADATA_CATALOGS:
        if ItemType == 'Attributes':
            PropList = Types.AttributePropertyList

    elif MetadataType == Types.METADATA_DOCUMENT:
        pass
    elif MetadataType == Types.METADATA_INFOREG:
        pass

    #Value = data[MetadataType][MetadataName][ItemType][PropertyName]
    Value = ''

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

@app.get("/{MetadataType}/{MetadataName}/{ItemType}/{PropertyName}/Attributes/{AttributeName}", tags=['Attributes'])
async def read_propertyTS7(
        MetadataType: str,
        MetadataName: str,
        ItemType: str,
        PropertyName : str  ,
        AttributeName : str  ,
        request: Request  ):

    PropList = Types.AttributePropertyList
    #Value = data[MetadataType][MetadataName][ItemType][PropertyName]['Attributes'][AttributeName]
    Value = ''
    res = {'requestPath': '/Catalogs/{dddd}/Property',
           Types.PROP_VALUE: Value,
           'PropertyList': PropList
           }
    return json.dumps(res)


@app.get("/css/", tags=['settings'])
async def read_CSS(request: Request):
    '''
    get a CSS file for MENU.HTML - metadata/menu.css
    :param request: NO
    :return: CSS-file as text
    '''

    myString = ''
    with open('metadata/menu.css', mode='r') as file:
        try:
            myString = file.read()
        except:
            myString = 'error'
    return myString

#**************************************
# DELETE METADATA SECTION
#**************************************

@app.delete('/{MetadataType}/{MetadataName}', tags=['Items'])
async def deleteItem_2(MetadataType: str, MetadataName : str):
    '''
    delete metadata of 2-th level - such as Catalogs, Documents and Information registers items
    :param MetadataType:
    :param MetadataName:
    :return: dictionary Result=True - as successfull case
    sample: /Catalogs/Goods
    '''

    #data[MetadataType].pop(MetadataName)
    return {'Result' : True}

@app.delete('/{MetadataType}/{MetadataName}/{lev1}/{lev2}', tags=['Items'])
async def deleteItem_4(MetadataType: str, MetadataName : str, lev1 : str, lev2 : str):
    '''
        delete metadata of 4-th level - such as Attributes items, Forms items etc.
        :param MetadataType:
        :param MetadataName:
        :param lev1:
        :param lev2:
        :return: dictionary Result=True - as successfull case
        sample: /Catalogs/Goods/Attributes/TableStyle
        '''

    #data[MetadataType][MetadataName][lev1].pop(lev2)
    return {'Result' : True}
@app.delete('/{MetadataType}/{MetadataName}/{lev1}/{lev2}/{lev3}', tags=['Items'])
async def deleteItem_5(MetadataType: str, MetadataName : str, lev1 : str, lev2 : str, lev3 : str):
    '''
         delete metadata of 5-th level - such as Attributes of Tabular sections
         :param MetadataType:
         :param MetadataName:
         :param lev1:
         :param lev2:
         :param lev3:
         :return: dictionary Result=True - as successfull case
         sample: /Catalogs/Goods/TabularSections/Goods/Description
         '''
    #data[MetadataType][MetadataName][lev1][lev2].pop(lev3)
    return {'Result' : True}



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
    '''
    read saved YAML config file from storage

    :return:
    '''
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


    newVal = EditItem()
    # dd = {Name: 'sdsdsd', Value: 'sss', Path: 'mytree1.Catalogs.Goods.Attributes.weight', PropertyName: 'Type', res: ''}
    # newVal.Name = ''
    newVal.Value = 'sss'
    newVal.ValueType = 'text'
    newVal.ValueAsBool = False
    newVal.ValueAsNumber = 0

    # newVal.PropertyPath = 'mytree1.Catalogs.Goods.Properties.Comment'
    newVal.PropertyName = 'Name'
    edit_one_MetadataName_property(newVal, new_struct)


def TestCreateItem():
    '''
      test function - to debug CreateItem process
      :return:
    '''

    TestData = CreateModel2()
    TestData.Path = 'mytree1.InformationRegisters.Attributes'
    TestData.Name = ''
    TestData.Result = False

    create_new_item_simple(TestData)


    #uvicorn.run(app, host="0.0.0.0", port=8000)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #create test date
    MD = Metadata.Metadata()

    newItem = MD.Catalogs.CreateObject('Goods')
    newAttr = newItem.Attributes.CreateObject('weight')

    newItem = MD.Catalogs.CreateObject('Departments')
    newAttr = newItem.Attributes.CreateObject('count')

    newAttr = newItem.Attributes.get('count')
    print(newAttr)

    newAttr = newItem.SetProperty('Comment', 'Hello')

    newForm = newItem.Forms.CreateObject()
    #newForm.


    MD.Documents.CreateObject()
    MD.Documents.CreateObject()

    MD.InformationRegisters.CreateObject()
    MD.InformationRegisters.CreateObject()

    print(MD.Catalogs)
    print(MD.Documents)
    print(MD.InformationRegisters)

    print('Tree:')
    #dd = myMetadata.GetTreeStructure()
    dd = myMetadata.Catalogs.GetItemByName('Goods')
    #dd = dd.GetTreeStructure()
    print(dd)

    #MD2 = Metadata.Metadata()
    #print(MD2.Catalogs)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



