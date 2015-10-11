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
          minterms_button = QPushButton("Minterms")
          maxterms_button = QPushButton("Maxterms")

          # Button events
          truth_table_button.clicked.connect(self.create_truth_table)

          # TODO: figure out if it is best to place minterms and maxterms information in
          # same window as the truth table or in separate windows
          
          grid.addWidget(truth_table_button, 1, 1, 1, 3)
          #grid.addWidget(minterms_button, 1, 2)
          #grid.addWidget(maxterms_button, 1, 3)
          
          grid.addWidget(function_label, 0, 0)
          grid.addWidget(self.function_input, 0, 1, 1, 3)

          grid.addWidget(instructions, 2, 0, 2, 2)

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

          # Might serve as display window for minterm and maxterm information as well
          # Maybe I'll try both cases and see what is best.
          
          function_output = function.solve()
          rows = len(function_output)
          columns = len(function_output[0])
          variables = function.get_variables()

          self.setWindowTitle("Truth Table")
          grid = QGridLayout()
          self.setLayout(grid)
          
          truth_table = QTableWidget(self)
          truth_table.setRowCount(rows)
          truth_table.setColumnCount(columns)

          for v in variables:
               truth_table.setHorizontalHeaderItem(variables.index(v), QTableWidgetItem(v))
          truth_table.setHorizontalHeaderItem(len(variables), QTableWidgetItem(str(function)))

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


          # Testing label interaction with table in window
          test_label = QLabel("Testing! f(x,y) = m1 + m2 = ~xy + x~y ")
          
          grid.addWidget(truth_table, 0, 0)
          grid.addWidget(test_label, 1, 0)
          self.resize(50 + 75*columns, 60 + 40*rows)
          

if __name__ == '__main__':
     app = QApplication(sys.argv)

     main_window = Main()
     main_window.show()

     sys.exit(app.exec_())

