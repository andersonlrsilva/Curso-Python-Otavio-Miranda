from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
import sys

app = QApplication()


# Botões
botao = QPushButton('texto do botão')
botao.setStyleSheet('font-size: 40px')

botao2 = QPushButton('texto do botão')
botao2.setStyleSheet('font-size: 40px')

botao3 = QPushButton('texto do botão')
botao3.setStyleSheet('font-size: 40px')

# widget Central (Janela principal da aplicação)
central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 2, 1, 1, 2)

central_widget.show()
app.exec()
