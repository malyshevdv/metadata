import unittest
import inspect
import metadata.src.Catalogs as Catalogs
import sys

def setUpModule():
    """called once, before anything else in this module"""
    print("START === In setUpModule()...")

def tearDownModule():
    """called once, after everything else in this module"""
    print("END === In tearDownModule()...")

class myTest01(unittest.TestCase):
    def test02(self):
        aa = 0
        print('Function => ' + inspect.stack()[0][3])

        self.assertTrue(aa == 0)

    def test01(self):
        aa = 0
        print('Function => ' + inspect.stack()[0][3])

        #self.assertFalse(aa == 0, msg='mistake heppened')

    @unittest.skipUnless(sys.platform.startswith("linux"), 'we need Windows')
    def test03(self):
        '''
        TEST CATALOGS FUNCTION ADD
        :return:
        '''
        self.assertEqual(Catalogs.addInfo(2,5),71, 'Error of eddition')
        print('Function => ' + inspect.stack()[0][3])
        print('HELLO')
        print(self.id())
        print(self.shortDescription())
        #self.assertFalse(aa == 0, msg='mistake heppened')

class myTest02_PROBA(unittest.TestCase):
    def test02_PRO(self):
        aa = 0
        print('Function => ' + inspect.stack()[0][3])

        self.assertTrue(aa == 0)
    @unittest.expectedFailure('test_item')
    def test01_BABA(self):
        #aa = 1/0
        print('Function => ' + inspect.stack()[0][3])

    @classmethod
    def setUpClass(cls):
        """called once, before any test"""
        print("In setUpClass()...")
    def setUp(self):
        """called multiple times, before every test method"""
        print("\nIn setUp()...")
    def tearDown(self):
        """called multiple times, after every test method"""
        print("In tearDown()...")






def suite():
    TestProc1 = myTest02_PROBA()

    test_suite = unittest.TestSuite()
    test_suite.addTest(myTest02_PROBA('test01_BABA'))
    test_suite.addTest(myTest02_PROBA('test02_PRO'))

    test_suite.addTest(unittest.makeSuite(myTest01))
    return test_suite

if __name__ == '__main__':
    #case1
    #unittest.main(verbosity=1)

    # case2
    runner = unittest.TextTestRunner()
    runner.run(suite())

    dd = 0
    print('The end')