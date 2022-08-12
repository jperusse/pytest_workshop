'''
    Module for calculator functions
'''


from math import prod


class Calc:
    '''
        Calc class will support these requirements
    '''

    def add(self, *list_obj):
        '''
            Adds numbers in a list object
        '''
        return sum(list_obj)

    def sub(self, first_parm, second_parm):
        '''
            Subtract second_parm from first_parm
        '''
        return first_parm - second_parm

    def mult(self, *list_obj):
        '''
            Multiply all elements of a list unless at least 1 is zero
        '''
        if 0 in list_obj:
            raise ValueError
        else:
            return prod(list_obj)

    def div(self, first_parm, second_parm):
        '''
            Divide first_parm by second_parm
        '''
        try:
            return first_parm / second_parm
        except ZeroDivisionError:
            return 'inf'
        return
