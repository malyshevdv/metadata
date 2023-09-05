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

AttributePropertyList = {
                'Name':{
                    'Type' : Types.STRING_TYPE,
                    'DefaultValue' : 'Catalog1'
                },
                'Type':{
                    'Type': Types.STRING_TYPE,
                    'DefaultValue': Types.STRING_TYPE
                },
                'DefaultValue':{
                    'Type': Types.STRING_TYPE,
                    'DefaultValue': ''
                },
                'MaxLength':{
                    'Type': Types.INTEGER_TYPE,
                    'DefaultValue': 50
                },
                'Precision':{
                    'Type': Types.INTEGER_TYPE,
                    'DefaultValue': 0
                },
                'Hierarchical':{
                    'Type': Types.BOOLEAN_TYPE,
                    'DefaultValue': False
                },
                'Index':{
                    'Type': Types.BOOLEAN_TYPE,
                    'DefaultValue': False
                },
                'Format':{
                    'Type': Types.STRING_TYPE,
                    'DefaultValue': ''
                },
                'EditionFormat':{
                    'Type': Types.STRING_TYPE,
                    'DefaultValue': ''
                },
                'ToolTip':{
                    'Type': Types.STRING_TYPE,
                    'DefaultValue': ''
                },
                'HighlightNegativeValue':{
                    'Type': Types.BOOLEAN_TYPE,
                    'DefaultValue': False
                },
                'MinimumValue':{
                    'Type': Types.INTEGER_TYPE,
                    'DefaultValue': 0
                },
                'MaximumValue':{
                    'Type': Types.INTEGER_TYPE,
                    'DefaultValue': 0
                },
                'Autofill':{
                    'Type': Types.BOOLEAN_TYPE,
                    'DefaultValue': False
                },
                'ReqiredField':{
                    'Type': Types.BOOLEAN_TYPE,
                    'DefaultValue': False
                }
 }
