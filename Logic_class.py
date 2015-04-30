''' Marcelo Autran '''
from collections import defaultdict

class Logic: 
    def __init__(self, value=True):
        ''' Constructor for Logic objects. Value defaults to True if no value is specified by user'''
        if int(value) == 1 or int(value) == 0:
            self.value = bool(value)
        else:
            raise TypeError("Logic class must be initialized with bool or int value")

    def __eq__(self, right):
        ''' Defines equality operator for operations between Logic objects and boolean values '''
        if type(right) == bool:
            return self.value == right
        elif isinstance(right, Logic):
            return self.value == right.value
        else:
            return False

    def __bool__(self):
        ''' Defines boolean representation of a Logic object '''
        return self.value

    def __str__(self):
        ''' Defines string representation of a Logic object '''
        return str(self.value)

    def __int__(self):
        ''' Defines integer representation of a Logic object '''
        return int(self.value)

    def __invert__(self):
        ''' Defines the complement(negation) operator for Logic objects '''
        return Logic(not self.value)

    def __add__(self,right):
        ''' Defines logical 'or' operation for Logic objects '''
        if isinstance(right, Logic) or type(right) == bool or right in [0,1]:
            return Logic(self.value or right)
        else:
            raise TypeError("unsupported operand type(s) for +: '"+ type(self).__name__+"' and '" + type(right).__name__ +"'")

    def __radd__(self, left):
        ''' 'or' operation for Logic objects on the right '''
        return self + left

    def __mul__(self, right):
        ''' Defines logical 'and' operation for Logic objects '''
        if isinstance(right, Logic) or type(right) == bool or right in [0,1]:
            return Logic(self.value and right)
        else:
            raise TypeError("unsupported operand type(s) for *: '"+ type(self).__name__+"' and '" + type(right).__name__ +"'")

    def __rmul__(self, left):
        ''' 'and' operation for Logic objects on the right '''
        return self*left

    def __xor__(self, right):
        ''' Defines logical 'xor' operator for Logic objects '''
        if isinstance(right, Logic) or type(right) == bool or right in [0,1]:
            return Logic(self.value ^ right)
        else:
            raise TypeError("unsupported operand type(s) for ^: '"+ type(self).__name__+"' and '" + type(right).__name__ +"'")

    def __rxor__(self, left):
        ''' 'xor' operation for Logic objects on the right '''
        return self^left

    def __pow__(self, right):
        ''' Defines logical 'nand' operator for Logic objects '''
        if isinstance(right, Logic) or type(right) == bool or right in [0,1]:
            return Logic(not (self.value * right))
        else:
            raise TypeError("unsupported operand type(s) for **: '"+ type(self).__name__+"' and '" + type(right).__name__ +"'")

    def __rpow__(self,left):
        ''' 'nand' operator for Logic objects on the right '''
        return self**left

    def __floordiv__(self, right):
        ''' Defines logical 'nor' operator for Logic objects '''
        if isinstance(right, Logic) or type(right) == bool or right in [0,1]:
            return Logic(not (self.value + right))
        else:
            raise TypeError("unsupported operand type(s) for //: '"+ type(self).__name__+"' and '" + type(right).__name__ +"'")

    def __rfloordiv__(self, left):
        ''' 'nor' operator for Logic objects on the left '''
        return self//left

    def __lt__(self, right):
        ''' Defines logical conditional operator (only if) for Logic objects '''
        if isinstance(right, Logic) or type(right) == bool or right in [0,1]:
            if bool(right) == False:
                return Logic(True)
            else:
                return Logic(self)
        else:
            raise TypeError("unsupported operand type(s) for >: '"+ type(self).__name__+"' and '" + type(right).__name__ +"'")
            
    def __ge__(self, right):
        ''' Defines biconditional operator (if and only if) for Logic objects '''
        if isinstance(right, Logic) or type(right) == bool or right in [0,1]:
            return Logic(self.value == bool(right))
        else:
            raise TypeError("unsupported operand type(s) for <=: '"+ type(self).__name__+"' and '" + type(right).__name__ +"'")

def _calculate(Logic_dict: dict, variable_list: [str], expression: str, c: int =0) -> [int]:
    ''' Recursive function that evaluates logical expressions of varying
    variable combinations. Returns result of expression given each possible
    permuation of varibale values '''
    result_list = []
    if c == len(Logic_dict):
        row_list = []
        for i in variable_list:
            row_list.append(int(Logic_dict[i]))
        row_list.append(int(eval(expression)))
        return row_list
    else:
        n = 0
        while n != 2:
            Logic_dict[variable_list[c]] = Logic(n)
            result_list.extend(_calculate(Logic_dict, variable_list, expression, c+1))
            n+= 1
        return result_list

##def _rowify(row_size, value_list: [int]) -> [[int]]:
##    ''' Converts a bigger list of values into a a list of smaller lists.
##    Makes the results of _calculate easier to parse for the the display fucntion '''
##    new_list = []
##    for i in range(pow(2, row_size-1)):
##        new_list.append(value_list[row_size*i:row_size*(i+1)])
##    return new_list
##
##def _parse_expression(expression: str, variable_list: [str]) -> str:
##    ''' Replaces the string characters in the expression with dictionary references '''
##    for i in variable_list:
##        expression = expression.replace(i, "Logic_dict['"+i+"']")
##    return expression
##
##def _evaluate(expression: str) -> [list]:
##    ''' Condenses the evaluation process of a logical expression
##    Returns all the expression's possible values '''
##    Logic_dict = _extract_objects(expression)
##    variable_list = sorted(list(Logic_dict.keys()))
##    return _calculate(Logic_dict, variable_list, _parse_expression(expression, variable_list))
##
##def _print_header(variable_list: [str], expression: str) -> None:
##    ''' Prints out the initial header for the truth table '''
##    header_str = ""
##    for i in variable_list:
##        header_str += "  "+i+"  |"
##    header_str += "  " + expression
##    print(header_str)
##    print("-"*len(header_str))
##
##def _display_truth_table(value_list: [[int]]) -> None:
##    ''' Display the list of values calculated from evaluate in a readable truth table format '''
##    for row in value_list:
##        row_str = ""
##        for i in range(len(row) - 1):
##            row_str += "  "+str(row[i])+"  |"
##        row_str += "  "+ str(row[-1])
##        print(row_str)
##
##def truth_table(expression: str) -> None:
##    ''' Prints out the truth table for a given logical expression '''
##    try:
##        Logic_dict = _extract_objects(expression)
##        variable_list = sorted(list(Logic_dict.keys()))
##        values = _calculate(Logic_dict, variable_list, _parse_expression(expression, variable_list))
##        _print_header(variable_list, expression)
##        _display_truth_table(_rowify(len(variable_list) +1, values))
##    except Exception as e:
##        print("ERROR")
##        print(e)
##
##def equivalence(expression1, expression2) -> bool:
##    if _extract_objects(expression1) == _extract_objects(expression2):
##        return _evaluate(expression1) == _evaluate(expression2)
##    else:
##        return False

def print_operators() -> None:
    ''' Prints out a list of supported operators '''
    print("""Logical operators supported:
    +  : OR
    *  : AND
    ~  : NOT
    ^  : XOR
    ** : NAND
    // : NOR
    >  : -> conditional (only if)
    <= : <-> biconditional (if and only if)
    """)


if __name__ == "__main__":
    print("Hi and Welcome to the Logic module! ")
    print_operators()
    
    
