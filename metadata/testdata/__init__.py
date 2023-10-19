import metadata.src.Metadata as Metadata
import metadata.src.Types as Types


def GetTestTree():

    #TestTree = {"Catalogs": {}, "Documents": {}, "InformationRegisters": {}}

    TestMD  = Metadata.Metadata()

# NEW OOP model

    newCatalogMD = TestMD.Catalogs.CreateObject('Goods')
    newCatalogMD.Attributes.CreateObject('comment', Types.AttributeTypes.STRING_TYPE)
    newCatalogMD.Attributes.CreateObject('weight', Types.AttributeTypes.NUMERIC_TYPE)

    newTab = newCatalogMD.TabularSections.CreateObject('Colors')
    newTab.Attributes.CreateObject('Good', Types.AttributeTypes.STRING_TYPE)
    newTab.Attributes.CreateObject('Count', Types.AttributeTypes.NUMERIC_TYPE)

    newCatalogMD.Forms.CreateObject('ObjectForm')
    newCatalogMD.Commands.CreateObject('OpenCommand')
    newCatalogMD.Templates.CreateObject('TemplateSchet')

    newCatalogMD = TestMD.Catalogs.CreateObject('Customers')
    newCatalogMD.Attributes.CreateObject('Adress', Types.AttributeTypes.STRING_TYPE)
    newCatalogMD.Attributes.CreateObject('EMail', Types.AttributeTypes.STRING_TYPE)




    newDocMD = TestMD.Documents.CreateObject('Invoice')

    newRegMD = TestMD.InformationRegisters.CreateObject('Curses')

    return TestMD

