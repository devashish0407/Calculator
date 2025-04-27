import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Simple Calculator')
        
        # Layouts
        vbox = QVBoxLayout()
        grid = QGridLayout()
        
        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(35)
        vbox.addWidget(self.display)
        
        # Buttons
        buttons = [
            ('7', 0, 0, 1, 1), ('8', 0, 1, 1, 1), ('9', 0, 2, 1, 1), ('/', 0, 3, 1, 1),
            ('4', 1, 0, 1, 1), ('5', 1, 1, 1, 1), ('6', 1, 2, 1, 1), ('*', 1, 3, 1, 1),
            ('1', 2, 0, 1, 1), ('2', 2, 1, 1, 1), ('3', 2, 2, 1, 1), ('-', 2, 3, 1, 1),
            ('0', 3, 0, 1, 1), ('.', 3, 1, 1, 1), ('=', 3, 2, 1, 1), ('+', 3, 3, 1, 1),
            ('C', 4, 0, 1, 4)  # 'C' button spans 4 columns
        ]

        for text, row, col, rowspan, colspan in buttons:
            button = QPushButton(text)
            button.setFixedSize(60, 40)
            button.clicked.connect(self.on_button_click)
            grid.addWidget(button, row, col, rowspan, colspan)

        vbox.addLayout(grid)
        self.setLayout(vbox)
    
    def on_button_click(self):
        button = self.sender()
        text = button.text()
        
        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText('Error')
        else:
            self.display.setText(self.display.text() + text)

# Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
