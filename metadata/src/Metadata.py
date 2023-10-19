import metadata.src.Types as Types

class Metadata:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Metadata, cls).__new__(cls)
        return cls._instance
    def __init__(self):
        self.Catalogs = CatalogsCollection()
        self.Documents = DocumentsCollection()
        self.InformationRegisters = InformationRegistersCollection()

    def GetTreeStructure(self):
        res = {
            "Catalogs" : self.Catalogs.GetTreeStructure(),
            "Documents": self.Documents.GetTreeStructure(),
            "InformationRegisters": self.InformationRegisters.GetTreeStructure()
        }
        return res


#*************************
# OBJECTS
#*************************
class MetadataObject:
    def __init__(self, Name, MetadataType = ''):
        self.__Properties = PropertyCollection(self)

        self.SetProperty('Name', Name)
        self.SetProperty('Synonym', Name)
        self.SetProperty('Comment', '')

        self.MetadataType = MetadataType
    def __repr__(self):
        return self.MetadataType + ' ' + self.GetProperty('Name')

    def SetProperty(self, propertyName, propertyValue):
        self.__Properties.SetProperty(propertyName, propertyValue)

    def GetProperty(self, propertyName):
        return self.__Properties.GetProperty(propertyName)

    def GetPropertyList(self) -> dict:
        PropertyList = {

            'Name': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': 'Catalog1'
            },
            'Synonyme': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': ''
            },
            'Comment': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': 'Catalog1'
            },
        }
        return PropertyList

    def GetTreeStructure(self):
        res = {}
        newRes = {}
        #for ii in self.__Properties:
        #    newRes[ii.Name] = ii.GetTreeStructure()
        #res["Properties"] = newRes

        return res

    def GenerateORM_Module(self):
        pass


class VisualObject(MetadataObject) :
    def __init__(self,Name, MetadataType = ''):
        super().__init__(Name, MetadataType)
        self.Forms = FormsCollection()
        self.Commands = CommandsCollection()
        self.Templates = TemplatesCollection()

    def GetTreeStructure(self):
        res = super.GetTreeStructure()
        return res

class Catalog(VisualObject):
    def __init__(self, Name):
        super().__init__(Name, 'Catalog')
        self.Attributes = AttributesCollection()
        self.TabularSections = TabularSectionsCollection()


    def GetPropertyList(self) -> dict :
        return Types.CatalogPropertyList


    def GetTreeStructure(self):
        res = super.GetTreeStructure()

        newRes = {}
        for ii in self.Forms:
            newRes[ii.Name] = ii.GetTreeStructure()
        res["Forms"] = newRes

        newRes = {}
        for ii in self.Templates:
            newRes[ii.Name] = ii.GetTreeStructure()
        res["Templates"] = newRes

        newRes = {}
        for ii in self.Commands:
            newRes[ii.Name] = ii.GetTreeStructure()
        res["Commands"] = newRes

        return res


class Document(VisualObject):
    def __init__(self,Name):
        super().__init__(Name, 'Document')
        self.Attributes = AttributesCollection()
        self.TabularSections = TabularSectionsCollection()

        self.Forms = FormsCollection()
        self.Commands = CommandsCollection()
        self.Templates = TemplatesCollection()
        pass
    def GetPropertyList(self) -> dict :
        return Types.DocumentPropertyList

class InformationRegister(VisualObject):
    def __init__(self, Name):
        super().__init__(Name, 'InformationRegister')
        self.Dimensions = AttributesCollection()
        self.Resourses = AttributesCollection()
        self.Attributes = AttributesCollection()

        self.Forms = FormsCollection()
        self.Commands = CommandsCollection()
        self.Templates = TemplatesCollection()

    def GetPropertyList(self) -> dict :
        return Types.InformationRegisterPropertyList

class TabularSection(MetadataObject):
    def __init__(self, Name):
        super().__init__(Name)
        self.Attributes = AttributesCollection()

class Attribute(MetadataObject):
    def __init__(self, Name, ItemType = ''):
        super().__init__(Name)
        if ItemType == '':
            self.SetProperty('Type', 'String')
        else:
            self.SetProperty('Type', ItemType)

    def GetPropertyList(self) -> dict :
        return Types.AttributePropertyList


class Form(MetadataObject):
    pass
class Command(MetadataObject):
    pass

class Template(MetadataObject):
    pass







#******************
#    COLLECTIONS
#******************

class ObjectCollection:
    def __init__(self):
        self._Items = {}
        self.NewObjectName = 'NewObject'
        self.ItemClass = MetadataObject

    def CreateObject(self, Name = '') -> MetadataObject:

        newName = Name
        if newName =='':
            newName = self.getNextName()

        newObject = self.ItemClass(newName)
        self._Items[newName] = newObject
        return newObject

    def getNextName(self) -> str:
        d = self.NewObjectName
        dd = str(len(self._Items)+1)
        return d + dd
    def get(self, Name):
        '''return object from dictionary by Name'''
        return self._Items.get(Name, None)

    def GetItemByName(self, ItemName):
        return self._Items[ItemName]

    def GetTreeStructure(self):
        res = {}
        for ind, Item in self._Items.items():
            res[ind] = Item.GetTreeStructure()
        return res

class CatalogsCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = Catalog
        self.NewObjectName = 'NewCatalog'

    def getPropertyList(self):
        return Types.CatalogPropertyList

class DocumentsCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = Document
        self.NewObjectName = 'NewDocument'


    def getPropertyList(self):
        return Types.DocumentPropertyList




class InformationRegistersCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = InformationRegister
        self.NewObjectName = 'NewInfoReg'
    def getPropertyList(self):
        return Types.InformationRegisterPropertyList

class TabularSectionsCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = TabularSection
        self.NewObjectName = 'NewTab'

    def getPropertyList(self):
        PropertyList = {
            'Name': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': 'Command1'
            },
            'Synonyme': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': ''
            },
            'Comment': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': 'Catalog1'
            }
        }
        return PropertyList

class AttributesCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = Attribute
        self.NewObjectName = 'NewAttribute'
    def CreateObject(self, Name = '', ItemType = ''):

        newName = Name
        if newName =='':
            newName = self.getNextName()

        newObject = self.ItemClass(newName, ItemType)
        self._Items[newName] = newObject
        return newObject
    def getPropertyList(self):
        AttributePropertyList = Types.AttributePropertyList
        return AttributePropertyList


class FormsCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = Form
        self.NewObjectName = 'NewForm'

class CommandsCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = Command
        self.NewObjectName = 'NewCommand'





class TemplatesCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = Template
        self.NewObjectName = 'NewTemplate'

class PropertyCollection:
    def __init__(self, BaseObject):
        self._Items = {}
        self.GetPropertyList = BaseObject.GetPropertyList
        self.BaseObject = BaseObject

    def SetProperty(self, propertyName : str, value):

        if self.GetPropertyList().get(propertyName, None) != None:
            self._Items[propertyName] = ProperyValue(propertyName, value, self.BaseObject)

    def GetProperty(self, propertyName : str):

        res = self._Items.get(propertyName, None)

        defValueStructure = self.GetPropertyList().get(propertyName, None)
        if  defValueStructure != None:
            pass

        return res.GetValue()

    def GetTreeStructure(self):
        return {}

class ProperyValue:
    def __init__(self, PropertyName, value, BaseObject):
        self.value = value
        self.BaseObject = BaseObject
    def GetValue(self):
        return self.value
    def SetValue(self, newValue):
        self.value = newValue

    def GetTreeStructure(self):
        return {}
