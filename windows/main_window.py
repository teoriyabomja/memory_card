from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import Qt
from PyQt5 import QtWidgets


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memory card')
        self.resize(600, 500)
        self.move(300, 300)

        self.result_layout = QtWidgets.QVBoxLayout()

        self.v_line1 = QtWidgets.QVBoxLayout()
        self.v_line2 = QtWidgets.QVBoxLayout()

        self.h_line = QtWidgets.QHBoxLayout()

        self.timer = QtWidgets.QSpinBox()
        self.timer.setValue(30)
        self.timer_lbl = QtWidgets.QLabel('хвилин')

        self.question_label = QtWidgets.QLabel('')
        self.correct_lbl = QtWidgets.QLabel('правильно')
        self.right_lbl = QtWidgets.QLabel('правильна відповідь')

        self.btn_menu = QtWidgets.QPushButton()
        self.btn_sleep = QtWidgets.QPushButton()

        self.r_btn1 = QtWidgets.QRadioButton('1')
        self.r_btn2 = QtWidgets.QRadioButton('2')
        self.r_btn3 = QtWidgets.QRadioButton('3')
        self.r_btn4 = QtWidgets.QRadioButton('4')

        self.answer_group_box = QtWidgets.QGroupBox('Варіанти відповідей:')
        self.radio_group_btn = QtWidgets.QButtonGroup()

        self.radio_group_btn.addButton(self.r_btn1)
        self.radio_group_btn.addButton(self.r_btn2)
        self.radio_group_btn.addButton(self.r_btn3)
        self.radio_group_btn.addButton(self.r_btn4)
        
        self.v_line1.addWidget(self.r_btn1)
        self.v_line1.addWidget(self.r_btn2)

        self.v_line2.addWidget(self.r_btn3)
        self.v_line2.addWidget(self.r_btn4)

        self.h_line.addLayout(self.v_line1)
        self.h_line.addLayout(self.v_line2)
        
        self.answer_group_box.setLayout(self.h_line)

        self.result_group_box = QtWidgets.QGroupBox()

        self.result_layout.addWidget(self.correct_lbl, alignment=(Qt.AlignLeft|Qt.AlignTop))
        self.result_layout.addWidget(self.right_lbl, alignment=Qt.AlignCenter, stretch=3)
        self.result_group_box.setLayout(self.result_layout)
        self.result_group_box.hide()

        self.setLayout(self.h_line)