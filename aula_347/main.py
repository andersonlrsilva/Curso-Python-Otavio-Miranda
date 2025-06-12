import sys
from PySide6.QtWidgets import QApplication, QLabel
from main_window import Mainwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()


label1 = QLabel('O meu texto')
label1.setStyleSheet('font-size: 150px;')
window.addWidgetToVlayout(label1)


window.show()
app.exec()
