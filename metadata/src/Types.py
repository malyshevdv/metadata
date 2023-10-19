'''
 Basic types and consts for work ather modules
 '''
from sqlalchemy import String, NUMERIC, Integer, Boolean
import metadata.src.Types as Types

class AttributeTypes:
    NUMERIC_TYPE = 'NUMERIC'
    STRING_TYPE = 'String'
    BOOLEAN_TYPE = 'Boolean'
    INTEGER_TYPE = 'Integer'
    DATETIME_TYPE = 'DateTime'


NUMERIC_TYPE = 'NUMERIC'
STRING_TYPE = 'String'
BOOLEAN_TYPE = 'Boolean'
INTEGER_TYPE = 'Integer'
DATETIME_TYPE = 'DateTime'

METADATA_CATALOGS = 'Catalogs'
METADATA_DOCUMENT = 'Documents'
METADATA_INFOREG = 'InformationRegisters'

PROP_NAME = 'Name'
PROP_SYNONYME = 'Synonyme'
PROP_COMMENT = 'Comment'

PROP_Properties = 'Properties'
PROP_Attributes = 'Attributes'
PROP_Resourses = 'Resourses'
PROP_Dimensions = 'Dimensions'

PROP_Tabulars = 'TabularSections'
PROP_Templates = 'Templates'
PROP_Commands = 'Commands'
PROP_Forms = 'Forms'


PROP_VALUE = 'Value'
PROP_DEFVALUE = 'DefaultValue'
PROP_TYPE = 'Type'

ATR_PROP_NAME_Name = 'Name'
ATR_PROP_NAME_Type = 'Type'
ATR_PROP_NAME_DefaultValue = 'DefaultValue'
ATR_PROP_NAME_MaxLength = 'MaxLength'
ATR_PROP_NAME_Precision = 'Precision'
ATR_PROP_NAME_Hierarchical = 'Hierarchical'
ATR_PROP_NAME_Index = 'Index'
ATR_PROP_NAME_Format = 'Format'
ATR_PROP_NAME_EditionFormat = 'EditionFormat'
ATR_PROP_NAME_MaxLength = 'MaxLength'
ATR_PROP_NAME_ToolTip = 'ToolTip'
ATR_PROP_NAME_HighlightNegativeValue = 'HighlightNegativeValue'
ATR_PROP_NAME_MinimumValue = 'MinimumValue'
ATR_PROP_NAME_MaximumValue = 'MaximumValue'
ATR_PROP_NAME_Autofill = 'Autofill'
ATR_PROP_NAME_ReqiredField = 'ReqiredField'


AttributeTypeList = ['Number', 'String', 'Boolean']
CodeTypeList = ['Number', 'String']


MetadataTypes = {
    METADATA_CATALOGS : {
        'NewItemName' : 'NewCatalog'
    },
    METADATA_DOCUMENT : {
        'NewItemName' : 'NewDocument'
    },
    METADATA_INFOREG : {
        'NewItemName': 'NewInformationRegister'
    },

    PROP_Attributes : {
        'NewItemName': 'NewAttribute'
    },
    PROP_Resourses: {
        'NewItemName': 'NewResourse'
    },
    PROP_Dimensions: {
        'NewItemName': 'NewDimension'
    },

    PROP_Forms: {
        'NewItemName': 'NewForm'
    },
    PROP_Commands: {
        'NewItemName': 'NewCommand'
    },
    PROP_Tabulars : {
        'NewItemName': 'NewTabularSection'
    },
    PROP_Templates: {
        'NewItemName': 'NewTemplate'
    }

}




def addProp(myOb, PropName, propType, DefValue, Selectable = False, SelectList = []):
    myOb[PropName] = PropertyItem(PropName, propType, DefValue, Selectable , SelectList)

class PropertyItem:
    def __init__(self, PropertyName, PropertyType, DefaultValue='', Selectable = False, SelectList=[]):
        self.Name = PropertyName
        self.SetType(PropertyType)
        self.DefaultValue = DefaultValue
        self.Selectable = Selectable
        self.SelectList = SelectList

    def GetSutableTypes(self):
        return []

    def SetType(self, PropertyType):
        self.Type = PropertyType

AttributePropertyList = {}
addProp(AttributePropertyList, ATR_PROP_NAME_Name ,            STRING_TYPE, 'Catalog1')
addProp(AttributePropertyList, ATR_PROP_NAME_Type ,            STRING_TYPE , Types.STRING_TYPE, True, AttributeTypeList)
addProp(AttributePropertyList, ATR_PROP_NAME_DefaultValue ,    STRING_TYPE , '')
addProp(AttributePropertyList, ATR_PROP_NAME_MaxLength ,       INTEGER_TYPE , 50 )
addProp(AttributePropertyList, ATR_PROP_NAME_Precision ,       INTEGER_TYPE , 0)
addProp(AttributePropertyList, ATR_PROP_NAME_Hierarchical ,    BOOLEAN_TYPE , False)
addProp(AttributePropertyList, ATR_PROP_NAME_Index ,           BOOLEAN_TYPE , False)
addProp(AttributePropertyList, ATR_PROP_NAME_Format ,          STRING_TYPE , "")
addProp(AttributePropertyList, ATR_PROP_NAME_EditionFormat ,   STRING_TYPE , '')
addProp(AttributePropertyList, ATR_PROP_NAME_ToolTip ,         STRING_TYPE , "")
addProp(AttributePropertyList, ATR_PROP_NAME_HighlightNegativeValue , BOOLEAN_TYPE , False)
addProp(AttributePropertyList, ATR_PROP_NAME_MinimumValue ,    INTEGER_TYPE , 0)
addProp(AttributePropertyList, ATR_PROP_NAME_MaximumValue ,    INTEGER_TYPE , 0)
addProp(AttributePropertyList, ATR_PROP_NAME_Autofill ,        BOOLEAN_TYPE , False)
addProp(AttributePropertyList, ATR_PROP_NAME_ReqiredField ,    BOOLEAN_TYPE , False)




OB_PROP_NAME_Name = 'Name'
OB_PROP_NAME_Synonyme = 'Synonyme'
OB_PROP_NAME_Comment = 'Comment'
OB_PROP_NAME_Hierarchical = 'Hierarchical'
OB_PROP_NAME_HierarchyType = 'HierarchyType'
OB_PROP_NAME_LimitNumberOfLevels = 'LimitNumberOfLevels'
OB_PROP_NAME_NumberOfLevels = 'NumberOfLevels'
OB_PROP_NAME_Owners = 'Owners'
OB_PROP_NAME_CodeLength = 'CodeLength'
OB_PROP_NAME_DescriptionLength = 'DescriptionLength'
OB_PROP_NAME_CodeType = 'CodeType'

OB_PROP_NAME_CheckUniqueness = 'CheckUniqueness'
OB_PROP_NAME_Autonumbering = 'Autonumbering'
OB_PROP_NAME_DefaultObjectForm = 'DefaultObjectForm'
OB_PROP_NAME_DefaultFolderForm = 'DefaultFolderForm'
OB_PROP_NAME_DefaultListForm = 'DefaultListForm'
OB_PROP_NAME_DefaultChoiceForm = 'DefaultChoiceForm'




CatalogPropertyList = {}

addProp(CatalogPropertyList, OB_PROP_NAME_Name, Types.STRING_TYPE, 'Catalog1')
addProp(CatalogPropertyList, OB_PROP_NAME_Synonyme, Types.STRING_TYPE , '')
addProp(CatalogPropertyList, OB_PROP_NAME_Comment, Types.STRING_TYPE , 'Catalog1')
addProp(CatalogPropertyList, OB_PROP_NAME_Hierarchical, Types.BOOLEAN_TYPE , False)
addProp(CatalogPropertyList, OB_PROP_NAME_HierarchyType, Types.STRING_TYPE , '')
addProp(CatalogPropertyList, OB_PROP_NAME_LimitNumberOfLevels, Types.BOOLEAN_TYPE ,False )
addProp(CatalogPropertyList, OB_PROP_NAME_NumberOfLevels, Types.INTEGER_TYPE , 2 )
addProp(CatalogPropertyList, OB_PROP_NAME_Owners, Types.STRING_TYPE , '')

addProp(CatalogPropertyList, OB_PROP_NAME_CodeLength, Types.INTEGER_TYPE , 9)

addProp(CatalogPropertyList, OB_PROP_NAME_DescriptionLength, Types.INTEGER_TYPE , 150)
addProp(CatalogPropertyList, OB_PROP_NAME_CodeType, Types.STRING_TYPE , 'String', True, Types.CodeTypeList)
addProp(CatalogPropertyList, OB_PROP_NAME_CheckUniqueness, Types.BOOLEAN_TYPE , True)
addProp(CatalogPropertyList, OB_PROP_NAME_Autonumbering, Types.BOOLEAN_TYPE , True)
addProp(CatalogPropertyList, OB_PROP_NAME_DefaultObjectForm, Types.STRING_TYPE , '')
addProp(CatalogPropertyList, OB_PROP_NAME_DefaultFolderForm, Types.STRING_TYPE , '')
addProp(CatalogPropertyList, OB_PROP_NAME_DefaultListForm, Types.STRING_TYPE , '')
addProp(CatalogPropertyList, OB_PROP_NAME_DefaultChoiceForm, Types.STRING_TYPE , '')

DocumentPropertyList = {

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

    'Numerator': {
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'NumeratorType': {
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'NumeratorLength.': {
        'Type': Types.INTEGER_TYPE,
        'DefaultValue': 9
    },

    'Periodicity': {
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'CheckUniqueness': {
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': True
    },
    'NumberOfLevels': {
        'Type': Types.INTEGER_TYPE,
        'DefaultValue': 2

    },
    'Owners': {
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'CodeLength': {
        'Type': Types.INTEGER_TYPE,
        'DefaultValue': 9
    },
    'DescriptionLength': {
        'Type': Types.INTEGER_TYPE,
        'DefaultValue': 150
    },
    'CodeType': {
        'Type': Types.STRING_TYPE,
        'DefaultValue': 'String'
    },
    'CheckUniqueness': {
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': True
    },
    'Autonumbering': {
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': True
    },
    'DefaultObjectForm': {
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'DefaultFolderForm': {
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'DefaultListForm': {
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'DefaultChoiceForm': {
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    }

}

InformationRegisterPropertyList = {
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

            'Periodicity': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': 'Nonperiodic'
            },

            'WriteMode': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': 'Independent'
            },

            'MainFilterByPeriod': {
                'Type': Types.BOOLEAN_TYPE,
                'DefaultValue': False
            },

            'RecordEditingForm': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': ''
            },

            'DefaultListForm': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': 'Independent'
            },

            'Note': {
                'Type': Types.STRING_TYPE,
                'DefaultValue': ''
            }
        }

TabularSectionPropertyList = {
    'Name':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': 'Catalog1'
    },
    'Synonyme':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'Comment':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': 'Catalog1'
    }
}

FormPropertyList = {
    'Name':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': 'Catalog1'
    },
    'Synonyme':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'Comment':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': 'Catalog1'
    }
}

BasicPropertyList = {
    'Name':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': 'Catalog1'
    },
    'Synonyme':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'Comment':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': 'Catalog1'
    }
}


CommandsPropertyList = {
    'Name':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': 'Command1'
    },
    'Synonyme':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'Comment':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': 'Catalog1'
    }
}

DimensionPropertyList = Types.AttributePropertyList
DimensionPropertyList['Master'] = {
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': False
        }
DimensionPropertyList['MainFilter'] = {
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': False
        }
DimensionPropertyList['NoEmptyValues'] = {
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': False
        }

ResoursesPropertyList = Types.AttributePropertyList


def CreateNewAttribute_Number(Name : str):
    '''
     Add new NUMBER-attribute element to metadata object
    '''
    NewItem = {
        ATR_PROP_NAME_Name: {PROP_VALUE: Name},
        ATR_PROP_NAME_Type: {PROP_VALUE: 'Number'},
        ATR_PROP_NAME_MaxLength: {PROP_VALUE: 15},
        ATR_PROP_NAME_Precision: {PROP_VALUE: 0},
        ATR_PROP_NAME_Format: {PROP_VALUE: ""},
        ATR_PROP_NAME_Index: {PROP_VALUE: False}
    }

    return NewItem

def CreateNewAttribute_String(Name : str):
    '''
     Add new STRING-attribute element to metadata object
    '''
    NewItem = {
        ATR_PROP_NAME_Name: {PROP_VALUE: Name},
        ATR_PROP_NAME_Type: {PROP_VALUE: 'String'},
        ATR_PROP_NAME_MaxLength: {PROP_VALUE: 50},
        ATR_PROP_NAME_Precision: {PROP_VALUE: 0},
        ATR_PROP_NAME_Format: {PROP_VALUE: ""},
        ATR_PROP_NAME_Index: {PROP_VALUE: False}
    }
    return NewItem


def CreateNewTabular(Name : str):
    '''
     Add new tabular section to metadata object
    '''
    newTabular = {
        PROP_Properties : {},
        PROP_Attributes : {}
    }

    newTabular[PROP_Properties]['Name'] = {PROP_VALUE  :Name}
    newTabular[PROP_Properties]['Synonym'] = {PROP_VALUE  : Name}
    newTabular[PROP_Properties]['Comment'] = {PROP_VALUE  :''}

    return newTabular

def CreateNewCommand(Name : str):
    '''
     Add new Command to metadata object
    '''
    NewItem = {
        'Name': {
            PROP_VALUE: Name
        },
        'Synonym': {
            PROP_VALUE: Name
        },
        'Comment': {
            PROP_VALUE: ''
        }
    }
    return NewItem

def CreateNewTemplate(Name : str):
    '''
     Add new template to metadata object with current unique name
    '''

    NewItem = {
        'Name': {
            PROP_VALUE: Name
        },
        'Synonym': {
            PROP_VALUE: Name
        },
        'Comment': {
            PROP_VALUE: ''
        }
    }
    return NewItem

def CreateNewForm(Name : str):
    '''
     Add new dialog form to metadata object with current unique name
    '''
    NewItem = {
        'Name': {
            PROP_VALUE: Name
        },
        'Synonym': {
            PROP_VALUE: Name
        },
        'Comment': {
            PROP_VALUE: ''
        }
    }
    return NewItem
