import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication(sys.argv)
win = QWidget()
win.resize(450, 280)

text = QLabel('Нажим чтобы узнать победителя')
craken = QLabel('Кракен')
ibottom = QPushButton('Нажми меня')

vcontainer = QVBoxLayout()



vcontainer.addWidget(text, alignment=Qt.AlignmentFlag.AlignCenter)
vcontainer.addWidget(craken, alignment=Qt.AlignmentFlag.AlignCenter)
vcontainer.addWidget(ibottom, alignment=Qt.AlignmentFlag.AlignCenter)

win.setLayout(vcontainer)

win.show()
sys.exit(app.exec())
