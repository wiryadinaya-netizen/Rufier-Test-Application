from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QLabel, QVBoxLayout, 
    QMessageBox, QRadioButton, QHBoxLayout)

from random import randint

app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Quiz App!")
main_window.resize(700, 200)

lbl_question = QLabel("Leonardo da Vinci berasal dari negara?")

rbtn_answer1 = QRadioButton("Perancis")
rbtn_answer2 = QRadioButton("Yunani")
rbtn_answer3 = QRadioButton("Italia")
rbtn_answer4 = QRadioButton("Jerman")

layout_row1 = QHBoxLayout()
layout_row1.addWidget(rbtn_answer1, alignment = Qt.AlignmentFlag.AlignCenter)
layout_row1.addWidget(rbtn_answer2, alignment = Qt.AlignmentFlag.AlignCenter)

layout_row2 = QHBoxLayout()
layout_row2.addWidget(rbtn_answer3, alignment = Qt.AlignmentFlag.AlignCenter)
layout_row2.addWidget(rbtn_answer4, alignment = Qt.AlignmentFlag.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addWidget(lbl_question, alignment = Qt.AlignmentFlag.AlignCenter)
layout_main.addLayout(layout_row1)
layout_main.addLayout(layout_row2)

#Button Functionality
def answer_true():
    victory_win = QMessageBox()
    victory_win.setText("Tepat sekali!")
    victory_win.exec_()

def answer_false():
    lose_win = QMessageBox()
    lose_win.setText("Coba lagi kawan.")
    lose_win.exec_()

rbtn_answer1.clicked.connect(answer_false)
rbtn_answer2.clicked.connect(answer_false)
rbtn_answer3.clicked.connect(answer_true)
rbtn_answer4.clicked.connect(answer_false)

main_window.setLayout(layout_main)
main_window.show()
app.exec_()