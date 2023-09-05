import metadata.src.Catalogs as Catalogs
import metadata.src.Documents as Documents
import metadata.src.InformationRegisters as InformationRegisters

def GetTestTree():

    TestTree = {"Catalogs": {}, "Documents": {}, "InformationRegisters": {}}

    #CATALOGS
    newCatalog = Catalogs.CreateDemo('Goods')
    TestTree['Catalogs']['Goods']= newCatalog

    newCatalog = Catalogs.CreateDemo('Cusomers')
    TestTree['Catalogs']['Cusomers'] = newCatalog

    #DOCUMENTS

    newDoc = Documents.CreateDemo('Invoice')
    TestTree['Documents']['Invoice'] = newDoc

    # information register

    newReg = InformationRegisters.CreateDemo('Curses')
    TestTree['InformationRegisters']['Curses'] = newReg


    return TestTree

