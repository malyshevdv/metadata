import metadata.src.Types as Types
import metadata.src.Commands as Commands
import metadata.src.Templates as Templates

PropertyList = {
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
    },
    'Hierarchical': {
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': False
    },
    'HierarchyType':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'LimitNumberOfLevels':{
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': False
    },
    'NumberOfLevels':{
        'Type': Types.INTEGER_TYPE,
        'DefaultValue': 2

    },
    'Owners':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'CodeLength':{
        'Type': Types.INTEGER_TYPE,
        'DefaultValue': 9
    },
    'DescriptionLength':{
        'Type': Types.INTEGER_TYPE,
        'DefaultValue': 150
    },
    'CodeType':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': 'String'
    },
    'CheckUniqueness':{
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': True
    },
    'Autonumbering':{
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': True
    },
    'DefaultObjectForm':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'DefaultFolderForm':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'DefaultListForm':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'DefaultChoiceForm':{
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
        "Name": {Types.PROP_VALUE  : "weight"},
        "type": {Types.PROP_VALUE  :'Number'},
        "length": {Types.PROP_VALUE  :15},
        "dim": {Types.PROP_VALUE  :0},
        'format': {Types.PROP_VALUE  :""},
        'indexed': {Types.PROP_VALUE  :False}
    }

    newItem['Attributes']['Fullname'] = {
        "Name": {Types.PROP_VALUE  :"Fullname"},
        "type": {Types.PROP_VALUE  :'String'},
        "length": {Types.PROP_VALUE  :50},
        "dim": {Types.PROP_VALUE  :0},
        "format": {Types.PROP_VALUE  :""},
        "indexed": {Types.PROP_VALUE  :False}
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