#unittest module

import pytest, unittest
import Metadata

@pytest.fixture()
def fixture01():
    #print("\nIn fixture01()...")
    pass
@pytest.mark.usefixtures('fixture01')
class TestClass_Catalogs(unittest.TestCase):

    @classmethod
    def setup_class(self):
        '''Inicialize metadata '''
        print("\nIn setup_class()...")
        self.MD = Metadata.Metadata()


    @classmethod
    def teardown_class(cls):
        print("\nIn teardown_class()...")

    def test_case01_(self):
        '''Number of new catalogs'''
        newCatalog1 = self.MD.Catalogs.CreateObject('Test1')
        self.assertEqual(len(self.MD.Catalogs.Items),1)
        newCatalog2 = self.MD.Catalogs.CreateObject('Test+2')
        self.assertEqual(len(self.MD.Catalogs.Items),2)

    def test_case02_(self):
        '''new attribute'''

        newItem = self.MD.Catalogs.getItemByName('Test1')
        not self.assertEqual(newItem, -1)

