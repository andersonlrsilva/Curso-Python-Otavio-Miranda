from PySide6.QtWidgets import QGridLayout, QPushButton, QWidget
from variables import MEDIUM_FONTE_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONTE_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass', 'specialButton')


class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
