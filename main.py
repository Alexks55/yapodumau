import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

def show_winner(t, t2):
    random_num = randint(1, 100)
    ramdom_num = str(random_num)
    t2.setText(ramdom_num)
    t.setText('Победитель:')

app = QApplication(sys.argv)
win = QWidget()
win.resize(450, 280)

text = QLabel('Нажим чтобы узнать победителя')
craken = QLabel('Кракен')
ibottom = QPushButton('сгенерировать победителя')

vcontainer = QVBoxLayout()



vcontainer.addWidget(text, alignment=Qt.AlignmentFlag.AlignCenter)
vcontainer.addWidget(craken, alignment=Qt.AlignmentFlag.AlignCenter)
vcontainer.addWidget(ibottom, alignment=Qt.AlignmentFlag.AlignCenter)

ibottom.clicked.connect(lambda: show_winner(text, craken))

win.setLayout(vcontainer)

win.show()
sys.exit(app.exec())
