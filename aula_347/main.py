import sys

from buttons import ButtonsGrid
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
    info = Info("Sua conta")
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
