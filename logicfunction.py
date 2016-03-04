from collections import defaultdict
import logic


class LogicFunction:
    def __init__(self, expression):
        if isinstance(expression, str):
            self.expression = expression
            self.logic_dict = _extract_objects(expression)
            self.variable_list = sorted(list(self.logic_dict))
            self.parsed_expression = _parse_expression(expression, self.variable_list)
            self.values = self.solve()
        else:
            raise TypeError("LogicFunction class must be initialized with string value")

    def __str__(self):
        ''' Defines string representaiton of a LogicFunction object. '''
        return self.expression
        
    def __eq__(self, right):
        ''' Defines equality operator for LogicFunction objects. Returns true if both LogicFunction objects
        have the same _calculate output values. '''
        if isinstance(right, Logic_function):
            if self.logic_dict == right.logic_dict:
                return self._calculate() == right._calculate()
            else:
                return False
            
    def _print_header(self):
        ''' Prints out the initial header for the truth table. '''
        header_str = ""
        for i in self.variable_list:
            header_str += "  "+i+"  |"
        header_str += "  " + self.expression
        print(header_str)
        print("-"*len(header_str))
    
    def _calculate(self, c = 0):
        ''' Eavaluates the LogicFunction for all possible variable values and returns
        a list with all the input/output combinations. '''
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
                self.logic_dict[self.variable_list[c]] = logic.Logic(n)
                result_list.extend(self._calculate(c+1))
                n+= 1
            return result_list

    def get_variables(self):
        ''' returns a list containing the symbolic variables in a LogicFunction. '''
        return self.variable_list

    def solve(self):
        ''' returns the result of _calculate as a list of lists '''
        raw_results = self._calculate()
        new_results = _rowify(len(self.variable_list)+1, raw_results)

        return new_results

    def truth_table(self):
        ''' Prints out the truth table of a LogicFunction in a nice, readable format. '''
        self._print_header()
        _display_truth_table(self.values)

    def maxterms(self):
        ''' Returns a lits of the maxterms and their indexes for a logical function. '''
        maxterms = []
        index = 0
        for i in self.values:
            if i[-1] == 0:
                term = '('
                for j in range(len(self.variable_list)):
                    if i[j] == 1:
                        term += str(self.variable_list[j]) + " + "
                    else:
                        term += "~"+str(self.variable_list[j]) + " + "
                maxterms.append([index, term[:-3] + ")"])
            index += 1
        return maxterms

    def minterms(self):
        ''' Returns a list of the minterms and their indexes for a logical function. '''
        minterms = []
        index = 0
        for i in self.values:
            if i[-1] == 1:
                term = '('
                for j in range(len(self.variable_list)):
                    if i[j] == 1:
                        term += str(self.variable_list[j])
                    else:
                        term += "~"+str(self.variable_list[j])
                minterms.append([index,term + ")"])
            index += 1
        return minterms
        

    def tautology(self):
        ''' Returns True if a LogicFunction is a tautology, False if not. '''
        return all(x[-1] == 1 for x in self.values)

    def contradiction(self):
        ''' Returns True if a LogicFunction is a contradiction, False if not. '''
        return all(x[-1] == 0 for x in self.values)
    

def _rowify(row_size, value_list: [int]) -> [[int]]:
    ''' Converts a bigger list of values into a a list of smaller lists.
    Makes the results of _calculate easier to parse. '''
    new_list = []
    for i in range(pow(2, row_size-1)):
        new_list.append(value_list[row_size*i:row_size*(i+1)])
    return new_list

def _extract_objects(expression: str) -> dict:
    ''' Returns dictionary of characters in expression and their corresponding Logic objects. '''
    object_dict = defaultdict(str)
    for i in expression:
        if i.isalpha():
            object_dict[i] = logic.Logic()
    return object_dict

def _parse_expression(expression: str, variable_list: [str]) -> str:
    ''' Replaces the string characters in the expression with dictionary references. '''
    parsed_expression = ''
    for c in expression:
        if c in variable_list:
            parsed_expression += "self.logic_dict['"+c+"']"
        else:
            parsed_expression += c
        
    return parsed_expression

def _display_truth_table(value_list: [[int]]) -> None:
    ''' Displays the list of values calculated from _calculate in a readable truth table format. '''
    for row in value_list:
        row_str = ""
        for i in range(len(row) - 1):
            row_str += "  "+str(row[i])+"  |"
        row_str += "  "+ str(row[-1])
        print(row_str)

if __name__ == "__main__":
    logic.print_operators()

