import metadata.src.Types as Types
import metadata.src.Commands as Commands
import metadata.src.Templates as Templates

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

PropertyList = {}

Types.addProp(PropertyList, OB_PROP_NAME_Name, Types.STRING_TYPE, 'Catalog1')
Types.addProp(PropertyList, OB_PROP_NAME_Synonyme, Types.STRING_TYPE , '')
Types.addProp(PropertyList, OB_PROP_NAME_Comment, Types.STRING_TYPE , 'Catalog1')
Types.addProp(PropertyList, OB_PROP_NAME_Hierarchical, Types.BOOLEAN_TYPE , False)
Types.addProp(PropertyList, OB_PROP_NAME_HierarchyType, Types.STRING_TYPE , '')
Types.addProp(PropertyList, OB_PROP_NAME_LimitNumberOfLevels, Types.BOOLEAN_TYPE ,False )
Types.addProp(PropertyList, OB_PROP_NAME_NumberOfLevels, Types.INTEGER_TYPE , 2 )
Types.addProp(PropertyList, OB_PROP_NAME_Owners, Types.STRING_TYPE , '')

Types.addProp(PropertyList, OB_PROP_NAME_CodeLength, Types.INTEGER_TYPE , 9)

Types.addProp(PropertyList, OB_PROP_NAME_DescriptionLength, Types.INTEGER_TYPE , 150)
Types.addProp(PropertyList, OB_PROP_NAME_CodeType, Types.STRING_TYPE , 'String', True, Types.CodeTypeList)
Types.addProp(PropertyList, OB_PROP_NAME_CheckUniqueness, Types.BOOLEAN_TYPE , True)
Types.addProp(PropertyList, OB_PROP_NAME_Autonumbering, Types.BOOLEAN_TYPE , True)
Types.addProp(PropertyList, OB_PROP_NAME_DefaultObjectForm, Types.STRING_TYPE , '')
Types.addProp(PropertyList, OB_PROP_NAME_DefaultFolderForm, Types.STRING_TYPE , '')
Types.addProp(PropertyList, OB_PROP_NAME_DefaultListForm, Types.STRING_TYPE , '')
Types.addProp(PropertyList, OB_PROP_NAME_DefaultChoiceForm, Types.STRING_TYPE , '')


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



def CreateDemo(Name : str):

    res = {}
    newItem = {
        "Properties": {},
        "Attributes": {},
        "TabularSections": {},
        "Templates": {},
        "Commands": {},
        "Forms": {}
    }

    newItem['Properties']['Name'] = {
        Types.PROP_VALUE : Name
    }
    newItem['Properties']['Synonyme'] = {
        Types.PROP_VALUE  : Name
    }

    # dd = {'Description': 'Goods'}

    newItem['Attributes']['weight'] = {
        Types.ATR_PROP_NAME_Name : {Types.PROP_VALUE  : "weight"},
        Types.ATR_PROP_NAME_Type : {Types.PROP_VALUE  :'Number'},
        Types.ATR_PROP_NAME_MaxLength : {Types.PROP_VALUE  :15},
        Types.ATR_PROP_NAME_Precision : {Types.PROP_VALUE  :0},
        Types.ATR_PROP_NAME_Format : {Types.PROP_VALUE  :""},
        Types.ATR_PROP_NAME_Index : {Types.PROP_VALUE  :False}
    }

    newItem['Attributes']['Fullname'] = {
        Types.ATR_PROP_NAME_Name : {Types.PROP_VALUE  :"Fullname"},
        Types.ATR_PROP_NAME_Type : {Types.PROP_VALUE  :'String'},
        Types.ATR_PROP_NAME_MaxLength : {Types.PROP_VALUE  :50},
        Types.ATR_PROP_NAME_Precision : {Types.PROP_VALUE  :0},
        Types.ATR_PROP_NAME_Format : {Types.PROP_VALUE  :""},
        Types.ATR_PROP_NAME_Index : {Types.PROP_VALUE  :False}
    }

    newItem['Forms']['ItemForm'] = {
        "Name": {Types.PROP_VALUE  :"ItemForm"}
    }

    # TABULAR
    newTabular = {
        Types.PROP_Properties : {},
        Types.PROP_Attributes : {}
    }

    newTabular[Types.PROP_Properties]['Name'] = {Types.PROP_VALUE  :'Goods'}
    newTabular[Types.PROP_Properties]['Synonym'] = {Types.PROP_VALUE  :'Goods'}
    newTabular[Types.PROP_Properties]['Comment'] = {Types.PROP_VALUE  :''}

    newTabular['Attributes']['Good'] = {
        'Name': {Types.PROP_VALUE :'Good'}
    }
    newTabular['Attributes']['Count'] = {
        'Name': {Types.PROP_VALUE :'Count'}
    }
    newTabular['Attributes']['Summ'] = {
        'Name': {Types.PROP_VALUE :'Summ'}
    }

    newItem['TabularSections']['Goods'] = newTabular

    # COMMAND
    newCommand = {
        'Name': {
            Types.PROP_VALUE  :'Open'
        },
        'Synonym': {
            Types.PROP_VALUE  :'Open'
        },
        'Comment': {
            Types.PROP_VALUE  :''
        }
    }

    newItem['Commands']['Open'] = newCommand

    newItem['Templates']['Template2'] = {
        'Name': {
            Types.PROP_VALUE  : 'Template2'
        }
    }

    return newItem