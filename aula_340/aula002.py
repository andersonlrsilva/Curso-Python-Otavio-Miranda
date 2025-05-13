from PySide6.QtWidgets import QApplication, QPushButton
import sys

app = QApplication()

botao = QPushButton('texto do botão')
botao.setStyleSheet('font-size: 40px')
botao.show()

app.exec()
