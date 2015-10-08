#Still experimenting with the PyQt5 framework and the different layouts.

import sys
import PyQt5.QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox,  
                             QHBoxLayout, QVBoxLayout, QMainWindow, QApplication)
import logicfunction

class Main(QWidget):
     def __init__(self):
          super().__init__()

          grid = QGridLayout()
          self.setLayout(grid)
##
##          hbox = QHBoxLayout()
##
##          vbox = QVBoxLayout()
##          vbox.addLayout(hbox)

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

          #font = QtGui.QFont("Tahoma", 10)
          #function.setFont(font)
          #instructions.setFont(font)
          
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

##          hbox.addWidget(function)
##          hbox.addWidget(function_input)
##
##          self.setLayout(vbox)
          
          self.setWindowTitle("Boolean Tools")
          self.setGeometry(300, 300, 400, 200)
          
     def create_truth_table(self):
          try:
               function_str = str(self.function_input.text())
               if function_str != '' :
                    print("In method")
                    print(function_str)
                    function = logicfunction.LogicFunction(function_str)
                    #results = function.calculate()

                    QMessageBox.about(self, "Display test!", str(function))
          except Exception as e:
               print(e)



if __name__ == '__main__':
     app = QApplication(sys.argv)

     main_window = Main()
     main_window.show()

     sys.exit(app.exec_())

