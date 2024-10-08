import sys

from PyQt6.QtWidgets import QPushButton, QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit

alphabet = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Азбука Морзе')

        self.result = QLineEdit()

        self.main_layout = QVBoxLayout()
        self.first_layout = QHBoxLayout()
        self.second_layout = QHBoxLayout()

        self.alphabet_buttons = {}

        for i in list(alphabet.keys())[:15]:
            btn = QPushButton(i)
            btn.clicked.connect(lambda checked, letter=i: self.addMorseCode(letter))
            self.alphabet_buttons[i] = btn
            self.first_layout.addWidget(btn)

        for i in list(alphabet.keys())[15:]:
            btn = QPushButton(i)
            btn.clicked.connect(lambda checked, letter=i: self.addMorseCode(letter))
            self.alphabet_buttons[i] = btn
            self.second_layout.addWidget(btn)

        self.main_layout.addLayout(self.first_layout)
        self.main_layout.addLayout(self.second_layout)
        self.main_layout.addWidget(self.result)

        self.setLayout(self.main_layout)

    def addMorseCode(self, letter):
        self.result.setText(self.result.text() + alphabet[letter])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = MorseCode()
    program.show()
    sys.exit(app.exec())






