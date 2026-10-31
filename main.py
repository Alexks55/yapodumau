import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.expression = ""

        self.setWindowTitle("Калькулятор")
        self.resize(350, 500)
        self.setStyleSheet(
            """
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-size: 18px;
            }
            QLineEdit {
                background-color: #2b2b2b;
                border: 1px solid #444;
                border-radius: 8px;
                padding: 12px;
                font-size: 28px;
                qproperty-alignment: AlignRight;
            }
            QPushButton {
                background-color: #3a3a3a;
                border: 1px solid #555;
                border-radius: 8px;
                min-height: 54px;
                font-size: 22px;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
            QPushButton#op {
                background-color: #f39c12;
                color: black;
            }
            QPushButton#eq {
                background-color: #2ecc71;
                color: black;
            }
            QPushButton#clear {
                background-color: #e74c3c;
            }
            """
        )

        main_layout = QVBoxLayout(self)
        self.display = QLineEdit("0")
        self.display.setReadOnly(True)
        main_layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for row_index, row in enumerate(buttons):
            for col_index, text in enumerate(row):
                button = QPushButton(text)
                if text in {"/", "*", "-", "+"}:
                    button.setObjectName("op")
                elif text == "=":
                    button.setObjectName("eq")
                elif text == "C":
                    button.setObjectName("clear")

                button.clicked.connect(lambda checked, value=text: self.on_button_click(value))
                grid.addWidget(button, row_index, col_index)

        main_layout.addLayout(grid)

    def on_button_click(self, value):
        if value == "C":
            self.expression = ""
            self.display.setText("0")
            return

        if value == "⌫":
            self.expression = self.expression[:-1]
            self.display.setText(self.expression if self.expression else "0")
            return

        if value == "=":
            self.calculate()
            return

        if value in {"/", "*", "-", "+", ".", "(", ")"} or value.isdigit():
            self.expression += value
            self.display.setText(self.expression)

    def calculate(self):
        if not self.expression:
            return

        try:
            result = eval(self.expression, {"__builtins__": None}, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.display.setText(str(result))
            self.expression = str(result)
        except Exception:
            self.display.setText("Ошибка")
            self.expression = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
