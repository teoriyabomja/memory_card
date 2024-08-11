from PyQt5 import QtWidgets
from windows.main_window import Window

import sys
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()