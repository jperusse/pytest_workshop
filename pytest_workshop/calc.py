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
        res = None
        if 0 in list_obj:
            raise ValueError
        else:
            res = prod(list_obj)
            if isinstance(res, int):
                return res
            else:
                raise TypeError
        return res


    def div(self, first_parm, second_parm):
        '''
            Divide first_parm by second_parm
        '''
        try:
            return first_parm / second_parm
        except ZeroDivisionError:
            return 'inf'
        return

    def avg(self, *iter_obj, ll=-999999, ul=999999):
        '''
            Calculate average of iterable object
            Use optional lower limit(ll) and upper limit(ul)
            to filter out elements of the iterable iter_obj.
        '''
        average = None
        if ul is None and ll is None:
            new_iter_obj = iter_obj
        else:
            new_iter_obj = []
            for element in iter_obj:
                if element > ll and element < ul:
                    new_iter_obj.append(element)

        total = self.add(*new_iter_obj)
        length = len(new_iter_obj)
        average = self.div(total, length)

        return average
