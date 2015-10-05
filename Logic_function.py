from collections import defaultdict
import Logic_class


class Logic_function:
    def __init__(self, expression):
        self.expression = expression
        self.logic_dict = _extract_objects(expression)
        self.variable_list = sorted(list(self.logic_dict))
        self.parsed_expression = _parse_expression(expression, self.variable_list)
        self.values = _rowify(len(self.variable_list) +1, self._calculate())

    def __eq__(self, right):
        ''' Defines equality operator for Logic_function objects. Returns true if both functions
        have the same output values. '''
        if isinstance(right, Logic_function):
            if self.logic_dict == right.logic_dict:
                return self._calculate() == right._calculate()
            else:
                return False

    def _calculate(self, c = 0):
        ''' Eavaluates the function for all possible variable values and returns
        a list with all the input/output combinations'''
        result_list = []
        if c == len(self.logic_dict):
            row_list = []
            for i in self.variable_list:
                row_list.append(int(self.logic_dict[i]))
            row_list.append(int(eval(self.parsed_expression)))
            return row_list
        else:
            n = 0
            while n != 2:
                self.logic_dict[self.variable_list[c]] = Logic_class.Logic(n)
                result_list.extend(self._calculate(c+1))
                n+= 1
            return result_list

    def _print_header(self):
        ''' Prints out the initial header for the truth table '''
        header_str = ""
        for i in self.variable_list:
            header_str += "  "+i+"  |"
        header_str += "  " + self.expression
        print(header_str)
        print("-"*len(header_str))

    def truth_table(self):
        ''' Prints out the truth table of a logical function in a nice, readable format '''
        self._print_header()
        _display_truth_table(self.values)

    def maxterms(self):
        ''' Returns a lits of the maxterms for a logical function '''
        maxterms = []
        for i in self.values:
            if i[-1] == 0:
                term = '('
                for j in range(len(self.variable_list)):
                    if i[j] == 1:
                        term += str(self.variable_list[j]) + " + "
                    else:
                        term += "~"+str(self.variable_list[j]) + " + "
                maxterms.append(term[:-3] + ")")
        return maxterms

    def minterms(self):
        ''' Returns a list of the minterms for a logical function '''
        minterms = []
        for i in self.values:
            if i[-1] == 1:
                term = '('
                for j in range(len(self.variable_list)):
                    if i[j] == 1:
                        term += str(self.variable_list[j])
                    else:
                        term += "~"+str(self.variable_list[j])
                minterms.append(term + ")")
        return minterms
        

    def tautology(self):
        ''' Returns True if a logical function is a tautology, False if not '''
        return all(x[-1] == 1 for x in self.values)

    def contradiction(self):
        ''' Returns True if a logical function is a contradiction, False if not '''
        return all(x[-1] == 0 for x in self.values)
    

def _rowify(row_size, value_list: [int]) -> [[int]]:
    ''' Converts a bigger list of values into a a list of smaller lists.
    Makes the results of _calculate easier to parse for the the display function '''
    new_list = []
    for i in range(pow(2, row_size-1)):
        new_list.append(value_list[row_size*i:row_size*(i+1)])
    return new_list

def _extract_objects(expression: str) -> dict:
    ''' Returns dictionary of characters in expression and their corresponding Logic objects '''
    object_dict = defaultdict(str)
    for i in expression:
        if i.isalpha():
            object_dict[i] = Logic_class.Logic()
    return object_dict

def _parse_expression(expression: str, variable_list: [str]) -> str:
    ''' Replaces the string characters in the expression with dictionary references '''
    for i in variable_list:
        expression = expression.replace(i, "self.logic_dict['"+i+"']")
    return expression

def _display_truth_table(value_list: [[int]]) -> None:
    ''' Display the list of values calculated from evaluate in a readable truth table format '''
    for row in value_list:
        row_str = ""
        for i in range(len(row) - 1):
            row_str += "  "+str(row[i])+"  |"
        row_str += "  "+ str(row[-1])
        print(row_str)

Logic_class.print_operators()

