
import math
from typing import TYPE_CHECKING
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import isNumOrDot, isEmpty, isValidNumber
from variables import MEDIUM_FONTE_SIZE


if TYPE_CHECKING:
    from main_window import Mainwindow
    from display import Display
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONTE_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        # lf.setProperty('cssClass', 'specialButton')


class ButtonsGrid(QGridLayout):
    def __init__(
            self, display: 'Display', info: 'Info', window: 'Mainwindow',
            *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'DEL', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.winddow = window
        self._equation = ''
        self._left = None
        self._right = None
        self._op = None
        self._equationInitialValue = 'Sua Conta'

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText((value))

    def _makeGrid(self):
        for rowNumber, rowData in enumerate(self._gridMask):
            for colunmNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, colunmNumber)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)  # type: ignore

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == 'DEL':
            self._connectButtonClicked(button, self.display.backspace)

        if text in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
            )

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        bottonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada.')
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = bottonText
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError('Conta incompleta.')
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:

            if '^' in self.equation and isinstance(self._left,  float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)

        except ZeroDivisionError:
            self._showError('Divisão por zero')

        except OverflowError:
            self._showError('Essa conta não pode ser realizada')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

        if result == 'error':
            self.left = None

    def _makeDialog(self, text):
        msgBox = self.winddow.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
