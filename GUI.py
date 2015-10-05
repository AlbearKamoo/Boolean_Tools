#Start of the GUI implementation. I decided to go with the PyQt5 framework!

import sys
import PyQt5.QtCore
from PyQt5.QtWidgets import QWidget, QApplication

class Test(QWidget):
     def __init__(self, parent=None):
         super(Test, self).__init__(parent)
         
         self.setWindowTitle("Testing!")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    test = Test()
    test.show()

    sys.exit(app.exec_())
