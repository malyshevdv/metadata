import metadata.src.Types as Types

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

    'Periodicity':{
        'Type': Types.STRING_TYPE,
        'DefaultValue': ''
    },
    'CheckUniqueness':{
        'Type': Types.BOOLEAN_TYPE,
        'DefaultValue': True
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

def CreateDemo(Name : str):

    newItem = {
        'Properties': {},
        'Attributes': {},
        'TabularSections': {},
        'Templates': {},
        'Forms': {},
        'Commands': {}
    }
    newItem['Properties']['Name'] = {Types.PROP_VALUE: Name}
    newItem['Properties']['Synonyme'] = {Types.PROP_VALUE: Name}


    newItem['Attributes']['Fullname'] = {
        "Name": {Types.PROP_VALUE:"Fullname"},
        "Type": {Types.PROP_VALUE:'String'},
        "Length": {Types.PROP_VALUE:50},
        "Dim": {Types.PROP_VALUE:0},
        "Format": {Types.PROP_VALUE:""},
        "Indexed": {Types.PROP_VALUE:False}
    }

    # TABULAR
    newTabular = {
        Types.PROP_Properties: {},
        Types.PROP_Attributes: {}
    }

    newTabular[Types.PROP_Properties]['Name'] = {Types.PROP_VALUE: 'Goods'}
    newTabular[Types.PROP_Properties]['Synonym'] = {Types.PROP_VALUE: 'Goods'}
    newTabular[Types.PROP_Properties]['Comment'] = {Types.PROP_VALUE: ''}

    newTabular['Attributes']['Good'] = {
        'Name': {Types.PROP_VALUE: 'Good'}
    }
    newTabular['Attributes']['Count'] = {
        'Name': {Types.PROP_VALUE: 'Count'}
    }
    newTabular['Attributes']['Summ'] = {
        'Name': {Types.PROP_VALUE: 'Summ'}
    }

    newItem['TabularSections']['Goods'] = newTabular

    #FORMS
    newItem['Forms']['DocumentForm'] = {
        "Name": {Types.PROP_VALUE: "DocumentForm"}
    }

    # COMMAND
    newCommand = {'Name': {Types.PROP_VALUE:'OpenDoc'},
                  'Synonym': {Types.PROP_VALUE:'OpenDoc'},
                  'Comment': {Types.PROP_VALUE:''},
                  'Attributes': {Types.PROP_VALUE:{}}
                  }

    newItem['Commands']['OpenDoc'] = newCommand
    newItem['Templates']['Template1'] = {'Name': {Types.PROP_VALUE:'Template1'}}

    return newItem