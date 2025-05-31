# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QMainWindow,
                               QVBoxLayout, QHBoxLayout, QGridLayout, QWidget)
import sys

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha Janela')


# Botões
botao1 = QPushButton('texto do botão')
botao1.setStyleSheet('font-size: 40px')

botao2 = QPushButton('texto do botão')
botao2.setStyleSheet('font-size: 40px')

botao3 = QPushButton('texto do botão')
botao3.setStyleSheet('font-size: 40px')


layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 2, 1, 1, 2)

# primeira ação menu


@Slot()
def slot_example(status_bar):
    print(123)
    status_bar.showMessage('O meu slot foi executado')


def outro_slot(checked):
    print('Ésta marcado?', checked)


def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


# statusbar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menubar
menu = window.menuBar()
primeiro_menu = menu.addMenu("Arquivo")
primeira_acao = primeiro_menu.addAction('Imprimir')
segunda_acao = primeiro_menu.addAction('Excluir')
segunda_acao.triggered.connect(lambda: slot_example(status_bar))


terceira_acao = primeiro_menu.addAction('Sair')
terceira_acao.setCheckable(True)
terceira_acao.toggled.connect(outro_slot)  # type: ignore
# terceira_acao.hovered.connect(terceiro_slot(terceira_acao))  # type:ignoredterceira_acao.hovered.connect(terceiro_slot(terceira_acao))  # type:ignored


botao1.clicked.connect(terceiro_slot(terceira_acao))


segundo_menu = menu.addMenu("Editar")
primeira_acao = segundo_menu.addAction('Cortar')

window.show()
app.exec()  # loop da aplicação
