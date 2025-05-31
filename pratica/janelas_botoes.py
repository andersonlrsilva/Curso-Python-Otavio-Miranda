from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                               QGridLayout, QLineEdit)
import sys


# Janela
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Meu Software')


# Botoes

botao1 = QPushButton('entrar')
botao1.setStyleSheet('font-size: 40px')

botao2 = QPushButton('sair')
botao2.setStyleSheet('font-size: 40px')

line_edit = QLineEdit()


# layout
layout = QGridLayout()
central_widget.setLayout(layout)


layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(line_edit, 2, 1, 1, 2)


window.show()
app.exec()
