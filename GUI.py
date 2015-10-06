#Still experimenting with the PyQt5 framework and the different layouts.

import sys
import PyQt5.QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QGridLayout,  
                             QHBoxLayout, QVBoxLayout, QMainWindow, QApplication)


class Main(QWidget):

     def __init__(self):
          super(Main, self).__init__()

          grid = QGridLayout()
          self.setLayout(grid)
##
##          hbox = QHBoxLayout()
##
##          vbox = QVBoxLayout()
##          vbox.addLayout(hbox)

          

          function = QLabel("Boolean Function: ")
          function_input = QLineEdit()

          

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

          grid.addWidget(truth_table_button, 1, 1)
          grid.addWidget(minterms_button, 1, 2)
          grid.addWidget(maxterms_button, 1, 3)
          
          grid.addWidget(function, 0, 0)
          grid.addWidget(function_input, 0, 1, 1, 3)

          grid.addWidget(instructions, 2, 0, 2, 2)

##          hbox.addWidget(function)
##          hbox.addWidget(function_input)
##
##          self.setLayout(vbox)
          
          self.setWindowTitle("Boolean Tools")
          self.setGeometry(300, 300, 400, 200)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = Main()
    main_window.show()

    sys.exit(app.exec_())
