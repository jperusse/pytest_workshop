'''
    Test the Calc class
'''
import pytest

from pytest_workshop.calc import Calc

bad_right_parm = [3, 'fred']
bad_right_and_left_parms = ['fred', ' was here']
bad_left_parm = ['fred', 3]

def manage_exceptions_using_pytest(op_type, exception_obj, list_obj, lower_t=None, upper_t=None):
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

            case "avg":
                calc_obj.avg(*list_obj, lt=lower_t, ut=upper_t)

    return

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


def test_add_using_non_numeric_right():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("add", TypeError, bad_right_parm)


def test_add_using_non_numeric_both():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("add", TypeError, bad_right_and_left_parms)


def test_add_using_non_numeric_left():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("add", TypeError, bad_left_parm)

def test_add_must_have_two():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("add", ValueError, [4])

def test_sub_must_have_two():
    '''
        Requirement 1.2
        Test subtraction - negative test
    '''
    manage_exceptions_using_pytest("sub", TypeError, [4])

def test_mult_must_have_two():
    '''
        Requirement 1.3
        Test multiplication - negative test
    '''
    manage_exceptions_using_pytest("mult", ValueError, [4])

def test_avg_must_have_two():
    '''
        Requirement 1.5
        Test multiplication - negative test
    '''
    manage_exceptions_using_pytest("avg", ValueError, [4])

def test_div_must_have_two():
    '''
        Requirement 1.4
        Test division - negative test
    '''
    manage_exceptions_using_pytest("div", TypeError, [4])


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

def test_mult_many_numbers_and_zero():
    '''
        Requirement 1.3.2
        Test Multiply of many numbers
        Verify ValueError gets raised
    '''
    manage_exceptions_using_pytest("mult", ValueError, range(100))


def test_mult_many_numbers_and_zero_last():
    '''
        Requirement 1.3.2
        Test Multiply many numbers
        Verify ValueError gets raised
    '''
    manage_exceptions_using_pytest("mult", ValueError, [1, 2, 3, 4, 0])


def test_mult_by_zero_raises_exception():
    '''
        Requirement 1.3.2
        Test Multiply many numbers
        Verify ValueError gets raised
    '''
    manage_exceptions_using_pytest("mult", ValueError, [1, 0, 3, 4, 0])


def test_mult_by_all_zero_raises_exception():
    '''
        Requirement 1.3.2
        Test Multiply many numbers
        Verify ValueError gets raised
    '''
    manage_exceptions_using_pytest("mult", ValueError, [0, 0, 0, 0, 0])


def test_mult_using_non_numeric_right():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("mult", TypeError, bad_right_parm)


def test_mult_using_non_numeric_both():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("mult", TypeError, bad_right_and_left_parms)


def test_mult_using_non_numeric_left():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("mult", TypeError, bad_left_parm)


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


def test_sub_using_non_numeric_right():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("sub", TypeError, bad_right_parm)


def test_sub_using_non_numeric_both():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("sub", TypeError, bad_right_and_left_parms)


def test_sub_using_non_numeric_left():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("sub", TypeError, bad_left_parm)


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


def test_div_using_non_numeric_right():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("div", TypeError, bad_right_parm)


def test_div_using_non_numeric_both():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("div", TypeError, bad_right_and_left_parms)


def test_div_using_non_numeric_left():
    '''
        Requirement 1.1
        Test addition - negative test
    '''
    manage_exceptions_using_pytest("div", TypeError, bad_left_parm)


def test_avg_using_non_numeric_right():
    '''
        Requirement 1.5
        Test average - negative test
    '''
    manage_exceptions_using_pytest("avg", TypeError, bad_right_parm)


def test_avg_using_non_numeric_both():
    '''
        Requirement 1.5
        Test average - negative test
    '''
    manage_exceptions_using_pytest("avg", TypeError, bad_right_and_left_parms)


def test_avg_using_non_numeric_left():
    '''
        Requirement 1.5
        Test average - negative test
    '''
    manage_exceptions_using_pytest("avg", TypeError, bad_left_parm)

def test_avg_using_non_iterable():
    '''
        Requirement 1.5
        Test average - negative test
    '''
    manage_exceptions_using_pytest("avg", TypeError, 123)


def test_avg_of_two_numbers():
    '''
        Requirement 1.5
        Test average
    '''
    calc_obj = Calc()

    res = calc_obj.avg(10, 20)
    assert res == 15


def test_avg_of_a_list_of_numbers():
    '''
        Requirement 1.5
        Test average
    '''
    calc_obj = Calc()

    nums = [6, 3, 5, 4]
    res = calc_obj.avg(*nums)
    assert res == 4.5


def test_avg_of_a_list_of_numbers_with_upper_limit():
    '''
        Requirement 1.5.1
        Test average
    '''
    calc_obj = Calc()

    nums = [2, 5, 12, 98]
    res = calc_obj.avg(*nums, ut=90)
    assert res == pytest.approx(6.33333)


def test_avg_of_a_list_of_numbers_with_lower_limit():
    '''
        Requirement 1.5.1
        Test average
    '''
    calc_obj = Calc()

    nums = [2, 5, 12, 98]
    res = calc_obj.avg(*nums, lt=3)
    assert res == pytest.approx(38.33333)


def test_avg_of_a_list_of_numbers_with_both_limits():
    '''
        Requirement 1.5.1
        Test average
    '''
    calc_obj = Calc()

    nums = [2, 5, 12, 98]
    res = calc_obj.avg(*nums, lt=3, ut=90)
    assert res == 8.5


def test_avg_of_a_list_of_numbers_with_both_limits_equality_same_elelment():
    '''
        Requirement 1.5.2
        Test average
    '''
    calc_obj = Calc()

    nums = [2, 5, 12, 98]
    res = calc_obj.avg(*nums, lt=5, ut=5)
    assert res == 5


def test_avg_of_a_list_of_numbers_with_both_limits_equality_end_elelments():
    '''
        Requirement 1.5.2
        Test average
    '''
    calc_obj = Calc()

    nums = [2, 5, 12, 98]
    res = calc_obj.avg(*nums, lt=2, ut=98)
    assert res == 29.25


def test_avg_of_a_list_of_negative_numbers_with_both_limits_equality_end_elelments():
    '''
        Requirement 1.5.2
        Test average
    '''
    calc_obj = Calc()

    nums = [-2, -5, -12, -98]
    res = calc_obj.avg(*nums, lt=-98, ut=-2)
    assert res == -29.25


def test_avg_of_a_list_of_zeros_in_thresholds():
    '''
        Requirement 1.5.1
        Test average
    '''
    calc_obj = Calc()

    nums = [0, 0, 0, 0]
    res = calc_obj.avg(*nums, lt=-2, ut=98)
    assert res == 0

def test_avg_using_positive_and_negative_with_lower_threshold():
    '''
        Requirement 1.5.1
        Test average
    '''
    calc_obj = Calc()

    nums = [-1, 0, 1]
    res = calc_obj.avg(*nums, lt=0)
    assert res == 0.5

def test_avg_using_positive_and_negative_with_upper_threshold():
    '''
        Requirement 1.5.1
        Test average
    '''
    calc_obj = Calc()

    nums = [-1, 0, 1]
    res = calc_obj.avg(*nums, ut=0)
    assert res == -0.5

def test_avg_of_a_list_of_zeros_out_of_thresholds():
    '''
        Requirement 1.5.1
        Test average
    '''
    manage_exceptions_using_pytest("avg", ValueError, [0, 0, 0, 0], lower_t=2, upper_t=98)



def test_add_of_empty_list():
    '''
        Requirement 1.1
        Test average
    '''
    manage_exceptions_using_pytest("add", ValueError, [])

def test_sub_of_empty_list():
    '''
        Requirement 1.2
        Test average
    '''
    manage_exceptions_using_pytest("sub", TypeError, [None, None])

def test_mult_of_empty_list():
    '''
        Requirement 1.5.3
        Test average
    '''
    manage_exceptions_using_pytest("mult", ValueError, [])

def test_div_of_empty_list():
    '''
        Requirement 1.5
        Test average
    '''
    manage_exceptions_using_pytest("div", TypeError, [None, None])

def test_avg_of_empty_list():
    '''
        Requirement 1.5.3
        Test average
    '''
    manage_exceptions_using_pytest("avg", ValueError, [])

def test_avg_of_empty_list_with_thresholds():
    '''
        Requirement 1.5.3
        Test average
    '''
    manage_exceptions_using_pytest("avg", ValueError, [], lower_t=2, upper_t=90)
