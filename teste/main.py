import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.Botao1.clicked.connect(self.func1)

    def func1(self):
        num1 = float(self.lineEdit.text())
        num2 = float(self.lineEdit_2.text())
        total = num1 * num2
        self.label1.setNum(total)
        self.lineEdit.clear()
        self.lineEdit_2.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
