# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sline.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 581)
        MainWindow.setStyleSheet(u"#wgt_graphic {\n"
"	background: #cccccc;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.wgt_graphics = QWidget(self.centralwidget)
        self.wgt_graphics.setObjectName(u"wgt_graphics")
        self.wgt_graphics.setGeometry(QRect(0, 40, 801, 541))
        self.wgt_mode = QWidget(self.centralwidget)
        self.wgt_mode.setObjectName(u"wgt_mode")
        self.wgt_mode.setGeometry(QRect(0, 0, 801, 41))
        self.lb_emp = QLabel(self.wgt_mode)
        self.lb_emp.setObjectName(u"lb_emp")
        self.lb_emp.setGeometry(QRect(0, 0, 41, 41))
        self.lb_point = QLabel(self.wgt_mode)
        self.lb_point.setObjectName(u"lb_point")
        self.lb_point.setGeometry(QRect(40, 0, 41, 41))
        self.lb_line = QLabel(self.wgt_mode)
        self.lb_line.setObjectName(u"lb_line")
        self.lb_line.setGeometry(QRect(80, 0, 41, 41))
        self.lb_arc = QLabel(self.wgt_mode)
        self.lb_arc.setObjectName(u"lb_arc")
        self.lb_arc.setGeometry(QRect(120, 0, 41, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_emp.setText("")
        self.lb_point.setText("")
        self.lb_line.setText("")
        self.lb_arc.setText("")
    # retranslateUi

