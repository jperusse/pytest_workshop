'''
    Test the calc class
'''

from pytest_workshop.calc import Calc


def test_add_two_numbers():
    '''
        Requirement 1.1 addition
        Test Sum 2 numbers
    '''
    calc_obj = Calc()
    res = calc_obj.add(4, 5)
    assert res == 9


def test_add_many_numbers():
    '''
        Requirement 1.1.1
        Test sum of many numbers
    '''
    calc_obj = Calc()
    sum_first_100 = range(100)
    res = calc_obj.add(*sum_first_100)
    assert res == 4950


def test_mult_two_numbers():
    '''
        Requirement 1.1 addition
        Test Multiply 2 numbers
    '''
    calc_obj = Calc()
    res = calc_obj.mult(4, 5)
    assert res == 20


def test_mult_many_numbers():
    '''
        Requirement 1.1.1
        Test Multiply of many numbers
    '''
    calc_obj = Calc()
    mult_first_10 = range(1, 10)
    res = calc_obj.mult(*mult_first_10)
    assert res == 362880


def test_mult_many_numbers_and_zero():
    '''
        Requirement 1.1.1
        Test Multiply of many numbers
    '''
    calc_obj = Calc()
    mult_first_10 = range(10)
    res = calc_obj.mult(*mult_first_10)
    assert res == 0


def test_mult_many_numbers_and_zero_last():
    '''
        Requirement 1.1.1
        Test Multiply of many numbers
    '''
    calc_obj = Calc()
    mult_first_10 = [1, 2, 3, 4, 0]
    res = calc_obj.mult(*mult_first_10)
    assert res == 0


def test_sub_two_positive_numbers():
    '''  Test subtraction '''
    calc_obj = Calc()
    res = calc_obj.sub(10, 3)
    assert res == 7


def test_sub_two_negatives():
    '''  Test subtraction '''
    calc_obj = Calc()
    res = calc_obj.sub(-10, -3)
    assert res == -7


def test_sub_positive_and_negative_numbers():
    '''  Test subtraction '''
    calc_obj = Calc()
    res = calc_obj.sub(-10, 3)
    assert res == -13


def test_sub_zero_and_positive_numbers():
    '''  Test subtraction '''
    calc_obj = Calc()
    res = calc_obj.sub(0, 3)
    assert res == -3


def test_sub_zero_and_negative_numbers():
    '''  Test subtraction '''
    calc_obj = Calc()
    res = calc_obj.sub(0, -3)
    assert res == 3

def test_add_using_non_numeric_left():
    ''' Test addition passing an invalid numeric value  '''
    calc_obj = Calc()

    res = calc_obj.add('fred', 3)
    assert res == TypeError
