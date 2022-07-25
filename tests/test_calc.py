'''
    Test the calc class
'''

from pytest_workshop.calc import Calc

'''
 Requirement
'''
def test_add_two_numbers():
    ''' Test Calc.add to sum 2 numbers '''
    c = Calc()

    res = c.add(4, 5)

    assert res == 9

