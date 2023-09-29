'''
Catalogs-module describe CONSTS and Classes to work with Catalogs
'''

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

def CreateNewItem(Name : str):
    '''
    Create a new metadata Catalog item in metadata tree with a current name.
    '''
    newItem = {
        "Properties": {},
        "Attributes": {},
        "TabularSections": {},
        "Templates": {},
        "Commands": {},
        "Forms": {}
    }

    newItem['Properties']['Name'] = {
        Types.PROP_VALUE: Name
    }
    newItem['Properties']['Synonyme'] = {
        Types.PROP_VALUE: Name
    }

    return newItem

def CreateDemo(Name : str):
    '''
    Create a new DEMO metadata Catalog item in
    metadata tree with a current name with predefines
    properties, tabular forms, commands.
    '''

    res = {}
    newItem = CreateNewItem(Name)

    # dd = {'Description': 'Goods'}

    newItem['Attributes']['weight'] = Types.CreateNewAttribute_Number('weight')

    newItem['Attributes']['Fullname'] = Types.CreateNewAttribute_String('Fullname')

    newItem['Forms']['ItemForm'] = Types.CreateNewForm('ItemForm')

    # TABULAR
    newTabular = Types.CreateNewTabular('Good')

    newTabular['Attributes']['Good'] = Types.CreateNewAttribute_String('Good')
    newTabular['Attributes']['Count'] = Types.CreateNewAttribute_Number('Count')
    newTabular['Attributes']['Summ'] = Types.CreateNewAttribute_Number('Summ')

    newItem['TabularSections']['Goods'] = newTabular

    # COMMAND
    newItem['Commands']['Open'] = Types.CreateNewCommand('Open')

    newItem['Templates']['Template2'] = Types.CreateNewTemplate('Template2')

    return newItem

def addInfo(x, y):
    print('Function => ')
    return x + y
