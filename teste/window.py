# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMenuBar,
    QPushButton,
    QStatusBar,
    QTextBrowser,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Botao1 = QPushButton(self.centralwidget)
        self.Botao1.setObjectName("Botao1")
        self.Botao1.setGeometry(QRect(7, 377, 75, 24))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(90, 377, 329, 22))
        self.label1 = QLabel(self.centralwidget)
        self.label1.setObjectName("label1")
        self.label1.setGeometry(QRect(19, 123, 505, 147))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(433, 377, 282, 22))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setGeometry(QRect(245, 337, 256, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.Botao1.setText(QCoreApplication.translate("MainWindow", "Calcular", None))
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "insira o tamanho do la\u00e7o", None
            )
        )
        self.label1.setText(QCoreApplication.translate("MainWindow", "painel1", None))
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "insira o tamanho da fita", None)
        )
        self.textBrowser.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Calcula a quantidade de la\u00e7os por fita</p></body></html>',
                None,
            )
        )

    # retranslateUi
