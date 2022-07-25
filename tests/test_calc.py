from pytest_workshop.calc import Calc

'''
    Test the calc class
'''

def test_add_two_numbers():
    ''' Test Calc.add '''
    c = Calc()

    res = c.add(4,5)

    assert res == 9
