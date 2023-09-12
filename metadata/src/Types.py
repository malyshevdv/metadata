from sqlalchemy import String, NUMERIC, Integer, Boolean
import metadata.src.Types as Types

NUMERIC_TYPE = 'NUMERIC'
STRING_TYPE = 'String'
BOOLEAN_TYPE = 'Boolean'
INTEGER_TYPE = 'Integer'
DATETIME_TYPE = 'DateTime'

METADATA_CATALOGS = 'Catalogs'
METADATA_DOCUMENT = 'Cocuments'
METADATA_INFOREG = 'InformationRegisters'

PROP_NAME = 'Name'
PROP_SYNONYME = 'Synonyme'
PROP_COMMENT = 'Comment'

PROP_Properties = 'Properties'
PROP_Attributes = 'Attributes'
PROP_Tabs = 'TabularSections'
PROP_Templetes = 'Templates'
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

def addProp(myOb, PropName, propType, DefValue, Selectable = False, SelectList = []):
    myOb[PropName] = {
            'Type': propType,
            'DefaultValue': DefValue
        }
    if Selectable :
        myOb[PropName]['Selectable'] = Selectable
        myOb[PropName]['SelectList'] = SelectList


addProp(AttributePropertyList, ATR_PROP_NAME_Name ,            Types.STRING_TYPE, 'Catalog1')
addProp(AttributePropertyList, ATR_PROP_NAME_Type ,            Types.STRING_TYPE , Types.STRING_TYPE, True, AttributeTypeList)
addProp(AttributePropertyList, ATR_PROP_NAME_DefaultValue ,    Types.STRING_TYPE , '')
addProp(AttributePropertyList, ATR_PROP_NAME_MaxLength ,       Types.INTEGER_TYPE , 50 )
addProp(AttributePropertyList, ATR_PROP_NAME_Precision ,       Types.INTEGER_TYPE , 0)
addProp(AttributePropertyList, ATR_PROP_NAME_Hierarchical ,    Types.BOOLEAN_TYPE , False)
addProp(AttributePropertyList, ATR_PROP_NAME_Index ,           Types.BOOLEAN_TYPE , False)
addProp(AttributePropertyList, ATR_PROP_NAME_Format ,          Types.STRING_TYPE , "")
addProp(AttributePropertyList, ATR_PROP_NAME_EditionFormat ,   Types.STRING_TYPE , '')
addProp(AttributePropertyList, ATR_PROP_NAME_ToolTip ,         Types.STRING_TYPE , "")
addProp(AttributePropertyList, ATR_PROP_NAME_HighlightNegativeValue , Types.BOOLEAN_TYPE , False)
addProp(AttributePropertyList, ATR_PROP_NAME_MinimumValue ,    Types.INTEGER_TYPE , 0)
addProp(AttributePropertyList, ATR_PROP_NAME_MaximumValue ,    Types.INTEGER_TYPE , 0)
addProp(AttributePropertyList, ATR_PROP_NAME_Autofill ,        Types.BOOLEAN_TYPE , False)
addProp(AttributePropertyList, ATR_PROP_NAME_ReqiredField ,    Types.BOOLEAN_TYPE , False)


