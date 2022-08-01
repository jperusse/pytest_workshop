'''
    Test the calc class
'''

from pytest_workshop.calc import Calc

''' Requirement 1.1 addition '''


def test_add_two_numbers():
    ''' Test Sum 2 numbers '''
    calc_obj = Calc()
    res = calc_obj.add(4, 5)
    assert res == 9


'''
 Requirement 1.1.1
'''


def test_add_many_numbers():
    '''  Test sum of many numbers '''
    calc_obj = Calc()
    sum_first_100 = range(100)
    res = calc_obj.add(*sum_first_100)
    assert res == 4950


def test_sub_two_numbers():
    '''  Test subtraction '''
    calc_obj = Calc()
    res = calc_obj.sub(10, 3)
    assert res == 7
