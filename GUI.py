#Still experimenting with the PyQt5 framework and the different layouts.

import sys
import PyQt5.QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox,  
                             QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QMainWindow, QApplication)
import logicfunction

class Main(QWidget):
     def __init__(self):
          super().__init__()

          grid = QGridLayout()
          self.setLayout(grid)

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

          truth_table_button.clicked.connect(self.create_truth_table)

          grid.addWidget(truth_table_button, 1, 1)
          grid.addWidget(minterms_button, 1, 2)
          grid.addWidget(maxterms_button, 1, 3)
          
          grid.addWidget(function_label, 0, 0)
          grid.addWidget(self.function_input, 0, 1, 1, 3)

          grid.addWidget(instructions, 2, 0, 2, 2)

          self.setWindowTitle("Boolean Tools")
          self.setGeometry(300, 300, 400, 200)
          
     def create_truth_table(self):
          try:
               function_str = str(self.function_input.text())
               if function_str != '' :
                    print("In method")
                    print(function_str)
                    function = logicfunction.LogicFunction(function_str)
                    function_output = function.solve()

                    self.tw = TableWindow(function_output)
                    self.tw.show()
          except Exception as e:
               print(e)

class TableWindow(QWidget):
     def __init__(self, function_output):
          super().__init__()

          self.function_output = function_output
          rows = len(self.function_output)
          columns = len(self.function_output[0])

          grid = QGridLayout()
          self.setLayout(grid)
          self.resize(150*columns, 60*rows)
          
          truth_table = QTableWidget(self)
          truth_table.setRowCount(rows)
          truth_table.setColumnCount(columns)
          
          for row in range(0,rows):
               for column in range(0, columns):
                    value = QTableWidgetItem(str(self.function_output[row][column]))
                    print(self.function_output[row][column])
                    print(str(row) + " " +str(column))

                    truth_table.setItem(row, column, value)

          grid.addWidget(truth_table, 0, 0)
          

if __name__ == '__main__':
     app = QApplication(sys.argv)

     main_window = Main()
     main_window.show()

     sys.exit(app.exec_())

