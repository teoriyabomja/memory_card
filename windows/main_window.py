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

        self.main_line = QtWidgets.QVBoxLayout()

        self.v_line1 = QtWidgets.QVBoxLayout()
        self.v_line2 = QtWidgets.QVBoxLayout()

        self.h_line = QtWidgets.QHBoxLayout()
        self.h1_line = QtWidgets.QHBoxLayout()
        self.h2_line = QtWidgets.QHBoxLayout()

        self.timer = QtWidgets.QSpinBox()
        self.timer.setValue(30)
        self.timer_lbl = QtWidgets.QLabel('хвилин')

        self.question_label = QtWidgets.QLabel('Питання')
        
        self.correct_lbl = QtWidgets.QLabel('правильно')
        self.right_lbl = QtWidgets.QLabel('правильна відповідь')

        self.btn_menu = QtWidgets.QPushButton('меню')
        self.h1_line.addStretch(2)
        self.btn_sleep = QtWidgets.QPushButton('відпочити')
        self.btn_answer = QtWidgets.QPushButton('Відповісти')

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

        self.h1_line.addWidget(self.btn_menu)
        self.h1_line.setStretch(2, 2)
        self.h1_line.addWidget(self.btn_sleep)
        self.h1_line.addWidget(self.timer)
        self.h1_line.addWidget(self.timer_lbl)

        self.main_line.addLayout(self.h1_line)
        self.main_line.addWidget(self.question_label, Qt.AlignCenter|Qt.AlignCenter)

        self.h2_line.addWidget(self.answer_group_box)
        self.h2_line.addWidget(self.result_group_box)


        self.main_line.addLayout(self.h2_line, stretch=4)
        self.main_line.setStretch(1, 1)
        self.main_line.addWidget(self.btn_answer)

        self.setLayout(self.main_line)
