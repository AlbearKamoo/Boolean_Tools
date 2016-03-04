# I chose the PyQt grid layout as it is more familiar to me.

import sys
import PyQt5.QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QAbstractItemView, QHeaderView,  
                             QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QMainWindow, QApplication)
import logicfunction

class Main(QWidget):
     def __init__(self):
          super().__init__()

          grid = QGridLayout()
          self.setLayout(grid)

          # Main user input 
          function_label = QLabel("Boolean Function: ")
          self.function_input = QLineEdit()

          instructions = QLabel("""List of logical operators supported:
    +  : OR
    *  : AND
    ~  : NOT
    ^  : XOR
    ** : NAND
    // : NOR
    >  : -> conditional (only if)
    <= : <-> biconditional (if and only if)
    """)          
          truth_table_button = QPushButton("Truth Table")

          # Button events
          truth_table_button.clicked.connect(self.create_truth_table)
          
          # Add widgets to grid
          grid.addWidget(truth_table_button, 1, 1, 1, 3)
          grid.addWidget(function_label, 0, 0)
          grid.addWidget(self.function_input, 0, 1, 1, 3)
          grid.addWidget(instructions, 2, 0, 2, 2)

          # Set window properties
          self.setWindowTitle("Boolean Tools")
          self.setGeometry(300, 300, 400, 200)
          
     def create_truth_table(self):
          ''' Creates a new window with the truth table information for the inputs provided in the main window. '''
          
          # Try/except block for debugging purposes, may remove later
          try:
               function_str = str(self.function_input.text())
               if function_str != '' :
                    function = logicfunction.LogicFunction(function_str)

                    self.tw = TableWindow(function)
                    self.tw.show()
          except Exception as e:
               print(e)

class TableWindow(QWidget):
     def __init__(self, function):
          super().__init__()
          
          function_output = function.solve()
          rows = len(function_output)
          columns = len(function_output[0])
          self.variables = function.get_variables()
          self.minterms = function.minterms()
          self.maxterms = function.maxterms()

          self.setWindowTitle("Truth Table")
          grid = QGridLayout()
          self.setLayout(grid)
          
          truth_table = QTableWidget(self)
          truth_table.setRowCount(rows)
          truth_table.setColumnCount(columns)

          for v in self.variables:
               truth_table.setHorizontalHeaderItem(self.variables.index(v), QTableWidgetItem(v))
          truth_table.setHorizontalHeaderItem(len(self.variables), QTableWidgetItem(str(function)))

          for i in range(0,len(function_output)):
               truth_table.setVerticalHeaderItem(i, QTableWidgetItem(str(i)))

          # Populates table
          for row in range(0,rows):
               for column in range(0, columns):
                    value = QTableWidgetItem(str(function_output[row][column]))

                    truth_table.setItem(row, column, value)
                    truth_table.setColumnWidth(column, 75)
               truth_table.setRowHeight(row, 40)

          # Makes table cells read-only
          truth_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

          #Makes table stretch when window is resized
          truth_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
          truth_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
     
          minterm_title = QLabel("Sum-of-minterms(CDNF): ")
          minterm_label = QLabel(self.get_minterm_string())

          maxterm_title = QLabel("Product-of-maxterms(CCNF): ")
          maxterm_label = QLabel(self.get_maxterm_string())
          
          grid.addWidget(truth_table, 0, 0)
          grid.addWidget(minterm_title, 1, 0)
          grid.addWidget(minterm_label, 2, 0)
          grid.addWidget(maxterm_title, 3, 0)
          grid.addWidget(maxterm_label, 4, 0)
          self.resize(50 + 75*columns, 120 + 40*rows)

     def get_minterm_string(self):
          minterm_string = 'f('
          for v in self.variables:
               minterm_string += str(v) + ','
          minterm_string = minterm_string[:-1] + ') = '

          for pair in self.minterms:
               minterm_string += 'm' + str(pair[0]) + ' + '
          minterm_string = minterm_string[:-3] + ' = '

          for pair in self.minterms:
               minterm_string += str(pair[1]) + ' + '
          minterm_string = minterm_string[:-3]

          return minterm_string

     def get_maxterm_string(self):
          maxterm_string = 'f('
          for v in self.variables:
               maxterm_string += str(v) + ','
          maxterm_string = maxterm_string[:-1] + ') = '

          for pair in self.maxterms:
               maxterm_string += 'M' + str(pair[0]) + '*'
          maxterm_string = maxterm_string[:-1] + ' = '

          for pair in self.maxterms:
               maxterm_string += str(pair[1]) 

          return maxterm_string
          

if __name__ == '__main__':
     app = QApplication(sys.argv)

     main_window = Main()
     main_window.show()

     sys.exit(app.exec_())

