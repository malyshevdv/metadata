def addInfo(x, y):
    print('Function => ')
    return x + y
def setUpModule():
    """called once, before anything else in this module"""
    print("START === In setUpModule()...")

def tearDownModule():
    """called once, after everything else in this module"""
    print("END === In tearDownModule()...")

def test02():
    aa = 0
    assert 2==3

def test01():
    aa = 0
    assert 1 == 1

    #self.assertFalse(aa == 0, msg='mistake heppened')

def test03():
    print('Function => ' )

    #self.assertFalse(aa == 0, msg='mistake heppened')

def test02_PRO():
    aa = 0
    print('Function => ' )



def test01_BABA():
    aa = 0


@classmethod
def setUpClass():
    """called once, before any test"""
    print("In setUpClass()...")
def setUp():
    """called multiple times, before every test method"""
    print("\nIn setUp()...")
def tearDown():
    """called multiple times, after every test method"""
    print("In tearDown()...")

if __name__ == '__main__2':
    #unittest.main(verbosity=3)
    print('test01')