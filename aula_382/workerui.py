# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worker.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_myWidget(object):
    def setupUi(self, myWidget):
        if not myWidget.objectName():
            myWidget.setObjectName(u"myWidget")
        myWidget.resize(580, 303)
        font = QFont()
        font.setPointSize(28)
        myWidget.setFont(font)
        self.gridLayoutWidget = QWidget(myWidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 3, 572, 288))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 9, 0)
        self.label1 = QLabel(self.gridLayoutWidget)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)

        self.label2 = QLabel(self.gridLayoutWidget)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)

        self.Button1 = QPushButton(self.gridLayoutWidget)
        self.Button1.setObjectName(u"Button1")

        self.gridLayout.addWidget(self.Button1, 1, 0, 1, 1)

        self.Button2 = QPushButton(self.gridLayoutWidget)
        self.Button2.setObjectName(u"Button2")

        self.gridLayout.addWidget(self.Button2, 1, 1, 1, 1)


        self.retranslateUi(myWidget)

        QMetaObject.connectSlotsByName(myWidget)
    # setupUi

    def retranslateUi(self, myWidget):
        myWidget.setWindowTitle(QCoreApplication.translate("myWidget", u"Form", None))
        self.label1.setText(QCoreApplication.translate("myWidget", u"TextLabel", None))
        self.label2.setText(QCoreApplication.translate("myWidget", u"TextLabel", None))
        self.Button1.setText(QCoreApplication.translate("myWidget", u"PushButton", None))
        self.Button2.setText(QCoreApplication.translate("myWidget", u"PushButton", None))
    # retranslateUi

