'''
    Test the calc class
'''
import pytest

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
        Requirement 1.3 addition
        Test Multiply 2 numbers
    '''
    calc_obj = Calc()
    res = calc_obj.mult(4, 5)
    assert res == 20


def test_mult_many_numbers():
    '''
        Requirement 1.3.1
        Test Multiply of many numbers
    '''
    calc_obj = Calc()
    mult_first_10 = range(1, 10)
    res = calc_obj.mult(*mult_first_10)
    assert res == 362880


def mult_manage_exceptions_using_pytest(op_type, exception_obj, list_obj):
    '''
        function to trap exception using pytest
    '''
    calc_obj = Calc()
    with pytest.raises(exception_obj):
        match op_type:
            case "add":
                calc_obj.add(*list_obj)

            case "sub":
                calc_obj.sub(*list_obj)

            case "mult":
                calc_obj.mult(*list_obj)

            case "div":
                calc_obj.div(*list_obj)

    return


def test_mult_many_numbers_and_zero():
    '''
        Requirement 1.3.2
        Test Multiply of many numbers
        Verify ValueError gets raised
    '''
    mult_manage_exceptions_using_pytest("mult", ValueError, range(10))

def test_mult_many_numbers_and_zero_last():
    '''
        Requirement 1.3.2
        Test Multiply many numbers
        Verify ValueError gets raised
    '''
    mult_manage_exceptions_using_pytest("mult", ValueError, [1, 2, 3, 4, 0])

def test_mult_by_zero_raises_exception():
    '''
        Requirement 1.3.2
        Test Multiply many numbers
        Verify ValueError gets raised
    '''
    mult_manage_exceptions_using_pytest("mult", ValueError, [1, 0, 3, 4, 0])

def test_sub_two_positive_numbers():
    '''
        Requirement 1.2
        Test subtraction
    '''
    calc_obj = Calc()
    res = calc_obj.sub(10, 3)
    assert res == 7


def test_sub_two_negatives():
    '''
        Requirement 1.2
        Test subtraction
    '''
    calc_obj = Calc()
    res = calc_obj.sub(-10, -3)
    assert res == -7


def test_sub_positive_and_negative_numbers():
    '''
        Requirement 1.2
        Test subtraction
    '''
    calc_obj = Calc()
    res = calc_obj.sub(-10, 3)
    assert res == -13


def test_sub_zero_and_positive_numbers():
    '''
        Requirement 1.2
        Test subtraction
    '''
    calc_obj = Calc()
    res = calc_obj.sub(0, 3)
    assert res == -3


def test_sub_zero_and_negative_numbers():
    '''
        Requirement 1.2
        Test subtraction
    '''
    calc_obj = Calc()
    res = calc_obj.sub(0, -3)
    assert res == 3


def test_add_using_non_numeric_right():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    calc_obj = Calc()

    res = calc_obj.add(3, 'fred')
    assert res == TypeError


def test_add_using_non_numeric_both():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    calc_obj = Calc()

    res = calc_obj.add('fred', ' was here')
    assert res == TypeError


def test_add_using_non_numeric_left():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    calc_obj = Calc()

    res = calc_obj.add('fred', 3)
    assert res == TypeError


def test_add_using_none():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    calc_obj = Calc()

    res = calc_obj.add(None, 3)
    assert res is TypeError


def test_divide_with_no_remainder():
    '''
        Requirement 1.4
        Test division
    '''
    calc_obj = Calc()

    res = calc_obj.div(6, 3)
    assert res == 2


def test_divide_return_float():
    '''
        Requirement 1.4.1
        Test division
    '''
    calc_obj = Calc()

    res = calc_obj.div(11, 2)
    assert res == 5.5
    assert isinstance(res, float)


def test_divide_return_inf():
    '''
        Requirement 1.4.2
        Test division
    '''
    calc_obj = Calc()

    res = calc_obj.div(11, 0)
    assert res == 'inf'
