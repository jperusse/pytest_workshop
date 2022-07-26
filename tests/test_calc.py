'''
    Test the calc class
'''

from pytest_workshop.calc import Calc

'''
 Requirement 1.1
'''


def test_add_two_numbers():
    ''' Test Sum 2 numbers '''
    c = Calc()
    res = c.add(4, 5)
    assert res == 9

'''
 Requirement 1.1.1
'''


def test_add_many_numbers():
    '''  Test sum of many numbers '''
    c = Calc()
    s = range(100)
    res = c.add(*s)
    assert res == 4950
