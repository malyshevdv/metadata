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
def CreateNewItem(Name : str):
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

    return newItem

def CreateDemo(Name : str):

    newItem = CreateNewItem(Name)

    newItem['Attributes']['Fullname'] = Types.CreateNewAttribute_String('Fullname')

    # TABULAR
    newTabular = Types.CreateNewTabular('Goods')

    newTabular['Attributes']['Good'] = Types.CreateNewAttribute_String('Good')
    newTabular['Attributes']['Count'] = Types.CreateNewAttribute_Number('Count')
    newTabular['Attributes']['Summ'] = Types.CreateNewAttribute_Number('Summ')

    newItem['TabularSections']['Goods'] = newTabular

    #FORMS
    newItem['Forms']['DocumentForm'] = Types.CreateNewForm('DocumentForm')

    # COMMAND
    newItem['Commands']['OpenDoc'] = Types.CreateNewCommand('OpenDoc')
    newItem['Templates']['Template1'] = Types.CreateNewTemplate('Template1')

    return newItem