from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import Qt
from PyQt5 import QtWidgets


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memory Card')
        self.resize(600, 500)
        self.move(300, 300)
        d = 2
    
    def open_menu(self):
        pass
