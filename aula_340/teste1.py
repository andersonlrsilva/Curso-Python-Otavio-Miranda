from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QScrollBar, QGridLayout, QWidget
import sys


app = QApplication()

# Botoes de interações
botao1 = QPushButton('Botão 1')
botao1.setStyleSheet('font-size: 40px;')
botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 35px;')

# Janela Central
central_widget = QWidget()

# layout da janela principal
layout = QGridLayout()
# setando o layout
central_widget.setLayout(layout)

layout.addWidget(botao1)
layout.addWidget(botao2)


central_widget.show()
app.exec()
