import sys

from buttons import Button, ButtonsGrid
from main_window import Mainwindow
from display import Display
from info import Info
from PySide6.QtWidgets import QApplication, QLineEdit
from PySide6.QtGui import QIcon
from styles import setupTheme
from variables import WINDOWS_ICON_PATH


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = Mainwindow()

    # Define o icone
    icon = QIcon(str(WINDOWS_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info("2.0 ^ 10.0 = 1024")
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # buttons
    button = Button('texto do botao')
    window.addWidgetToVLayout(button)

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
