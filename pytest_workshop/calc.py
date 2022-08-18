'''
    Module for calculator functions
'''


from math import prod
import numbers


class Calc:
    '''
        Calc class will support these requirements
    '''

    def add(self, *list_obj):
        '''
            Adds numbers in a list object
        '''
        if len(list_obj) < 2:
            raise ValueError

        return sum(list_obj)

    def sub(self, first_parm, second_parm):
        '''
            Subtract second_parm from first_parm
        '''
        if not (isinstance(first_parm, numbers.Real) and isinstance(second_parm, numbers.Real)):
            raise TypeError
        else:
            return first_parm - second_parm

    def mult(self, *list_obj):
        '''
            Multiply all elements of a list unless at least 1 is zero
        '''
        if len(list_obj) < 2:
            raise ValueError

        res = None
        if 0 in list_obj:
            raise ValueError
        else:
            res = prod(list_obj)
            if isinstance(res, numbers.Real):
                return res
            else:
                raise TypeError
        return res


    def div(self, first_parm, second_parm):
        '''
            Divide first_parm by second_parm
        '''
        if not (isinstance(first_parm, int) and isinstance(second_parm, int)):
            raise TypeError
        else:
            try:
                return first_parm / second_parm
            except ZeroDivisionError:
                return 'inf'
        return

    def avg(self, *iter_obj, lt=None, ut=None):
        '''
            Calculate average of iterable object
            Use optional lower threshold(lt) and upper threshold(ut)
            to filter out elements of the iterable iter_obj.
        '''
        if len(iter_obj) < 2:
            raise ValueError

        if lt is None:
            lt = min(iter_obj)

        if ut is None:
            ut = max(iter_obj)

        average = None
        new_iter_obj = []
        for element in iter_obj:
            if element >= lt and element <= ut:
                new_iter_obj.append(element)

        total = sum(new_iter_obj)
        length = len(new_iter_obj)
        if length == 0:
            raise ValueError

        average = total / length

        return average
