'''
 Basic types and consts for work ather modules
 '''
from sqlalchemy import String, NUMERIC, Integer, Boolean
import metadata.src.Types as Types

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

AttributePropertyList = {}

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
    myOb[PropName] = {
            'Type': propType,
            'DefaultValue': DefValue
        }
    if Selectable :
        myOb[PropName]['Selectable'] = Selectable
        myOb[PropName]['SelectList'] = SelectList


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
