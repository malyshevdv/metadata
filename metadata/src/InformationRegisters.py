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

def CreateDemo(Name : str):

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

    newAttribute = {
        "Name": "weight",
        "type": 'Number',
        "length": 15,
        "dim": 0,
        'format': "",
        'indexed': False
    }
    newItem['Dimensions'][newAttribute['Name']] = newAttribute


    newAttribute2 = {
        "Name": "age",
        "type": 'Number',
        "length": 15,
        "dim": 0,
        'format': "",
        'indexed': False
    }
    newItem['Resourses'][newAttribute2['Name']] = newAttribute2

    newAttribute = {
        "Name": {Types.PROP_VALUE:"Name"},
        "type": {Types.PROP_VALUE:'String'},
        "length": {Types.PROP_VALUE:15},
        "dim": {Types.PROP_VALUE:0},
        'format': {Types.PROP_VALUE:""},
        'indexed': {Types.PROP_VALUE:False}
    }
    newItem['Attributes']['Name'] = newAttribute


    newItem['Forms']['DocumentForm'] = {
        "Name": {Types.PROP_VALUE:"DocumentForm"}
    }

    # COMMAND
    newCommand = {'Name': {Types.PROP_VALUE:'OpenRegister'},
                  'Synonym': {Types.PROP_VALUE:'Open'},
                  'Comment': {Types.PROP_VALUE:''}
                  }
    newItem['Commands']['OpenRegister'] = newCommand
    newItem['Templates']['Template1'] = {'Name': {Types.PROP_VALUE:'Template3'}}

    return newItem