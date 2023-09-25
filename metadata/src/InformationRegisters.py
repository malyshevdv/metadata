'''
InfoRegs-module describe CONSTS and Classes to work with Information registers
'''
import metadata.src.Catalogs as Catalogs
import metadata.src.Types as Types

AttributePropertyList = Types.AttributePropertyList

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

def CreateNewItem(Name : str):
    '''
     Add new information register with current unique name
    '''

    newItem = {
        'Properties': {},
        'Dimensions': {},
        'Resourses': {},
        'Attributes': {},
        'Templates': {},
        'Commands': {},
        'Forms': {}
    }
    newItem['Properties']['Name'] = {'Value': Name}
    newItem['Properties']['Synonym'] = {'Value': Name}
    newItem['Properties']['Comment'] = {'Value': ""}

    return newItem

def CreateDemo(Name : str):
    '''
     Create new DEMO information register with current unique name with predefined properties
    '''


    newItem = CreateNewItem(Name)

    newItem['Dimensions']['weight'] = Types.CreateNewAttribute_Number('weight')
    newItem['Dimensions']['age'] = Types.CreateNewAttribute_Number('age')

    newItem['Attributes']['Name'] = Types.CreateNewAttribute_String('Name')

    newItem['Forms']['DocumentForm'] = Types.CreateNewForm('DocumentForm')

    # COMMAND
    newItem['Commands']['OpenRegister'] = Types.CreateNewCommand('OpenRegister')
    newItem['Templates']['Template1'] = Types.CreateNewTemplate('Template1')

    return newItem