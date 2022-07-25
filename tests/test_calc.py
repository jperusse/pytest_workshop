'''
    Test the calc class
'''

from pytest_workshop.calc import Calc


def test_add_two_numbers():
    ''' Test Calc.add '''
    c = Calc()

    res = c.add(4, 5)

    assert res == 9
