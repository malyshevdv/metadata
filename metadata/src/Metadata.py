class Metadata:
    def __init__(self):
        self.Catalogs : dict = CatalogsCollection()
        self.Documents: dict = DocumentsCollection()
        self.InformationRegisters: dict = InformationRegistersCollection()

#******************
#    COLLECTIONS
#******************
class ObjectCollection:
    def __init__(self):
        self.Items = {}
        self.NewObjectName = 'NewObject'
        self.ItemClass = MetadataObject

    def CreateObject(self):
        newName = self.GetNextName()
        newObject = self.ItemClass(newName)
        self.Items[newName] = newObject
        return newObject

    def GetNextName(self):
        d = self.NewObjectName
        dd = str(len(self.Items)+1)
        return d + dd


class CatalogsCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = Catalog
        self.NewObjectName = 'NewCatalog'


class DocumentsCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = Document
        self.NewObjectName = 'NewDocument'

class InformationRegistersCollection(ObjectCollection):
    def __init__(self):
        super().__init__()
        self.ItemClass = InformationRegister
        self.NewObjectName = 'NewInfoReg'

class TabularSectionsCollection:
    def __init__(self):
        super().__init__()
        self.ItemClass = TabularSection
        self.NewObjectName = 'NewTab'

class AttributesCollection:
    def __init__(self):
        super().__init__()
        self.ItemClass = Attribute
        self.NewObjectName = 'NewAttribute'

class FormsCollection:
    def __init__(self):
        super().__init__()
        self.ItemClass = Form
        self.NewObjectName = 'NewForm'

class CommandsCollection:
    def __init__(self):
        super().__init__()
        self.ItemClass = Command
        self.NewObjectName = 'NewCommand'

class TemplatesCollection:
    def __init__(self):
        super().__init__()
        self.ItemClass = Template
        self.NewObjectName = 'NewTemplate'

#*************************
# OBJECTS
#*************************
class MetadataObject:
    def __init__(self, Name):
        self.Properties = {}

        self.Properties['Name'] = Name
        self.Properties['Synonym'] = Name
        self.Properties['Comment'] = ''

    def GetPropertyList(self) -> dict :
        return {}

    def GetObjectStructure(self):
        '''
        Get object JSON
        :return: JSON
        '''
        pass

    def GenerateORM_Module(self):
        pass


class VisualObject(MetadataObject) :
    def __init__(self,Name):
        super().__init__(Name)
        self.Forms = FormsCollection()
        self.Commands = CommandsCollection()
        self.Templates = TemplatesCollection()

class Catalog(VisualObject):
    def __init__(self,Name):
        super().__init__(Name)
        self.Attributes = AttributesCollection()
        self.TabularSections = TabularSectionsCollection()
    def GetPropertyList(self) -> dict :
        return Catalogs.PropertyList

class Document(VisualObject):
    def __init__(self,Name):
        super().__init__(Name)
        self.Attributes = AttributesCollection()
        self.TabularSections = TabularSectionsCollection()

        self.Forms = FormsCollection()
        self.Commands = CommandsCollection()
        self.Templates = TemplatesCollection()
        pass
    def GetPropertyList(self) -> dict :
        return Documents.PropertyList

class InformationRegister(VisualObject):
    def __init__(self, Name):
        super().__init__(Name)
        self.Dimensions = AttributesCollection()
        self.Resourses = AttributesCollection()
        self.Attributes = AttributesCollection()

        self.Forms = FormsCollection()
        self.Commands = CommandsCollection()
        self.Templates = TemplatesCollection()

    def GetPropertyList(self) -> dict :
        return InformationRegisters.PropertyList

class TabularSection(MetadataObject):
    def __init__(self, Name):
        super().__init__(Name)
        self.Attributes = AttributesCollection()

class Attribute(MetadataObject):
    pass
class Form(MetadataObject):
    pass
class Command(MetadataObject):
    pass

class Template(MetadataObject):
    pass

