# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'falsa.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(958, 723)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.funcion = QtGui.QLineEdit(self.centralwidget)
        self.funcion.setObjectName(_fromUtf8("funcion"))
        self.horizontalLayout.addWidget(self.funcion)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.a = QtGui.QLineEdit(self.centralwidget)
        self.a.setObjectName(_fromUtf8("a"))
        self.horizontalLayout.addWidget(self.a)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.b = QtGui.QLineEdit(self.centralwidget)
        self.b.setObjectName(_fromUtf8("b"))
        self.horizontalLayout.addWidget(self.b)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.tolerancia = QtGui.QLineEdit(self.centralwidget)
        self.tolerancia.setObjectName(_fromUtf8("tolerancia"))
        self.horizontalLayout.addWidget(self.tolerancia)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.cifras = QtGui.QLineEdit(self.centralwidget)
        self.cifras.setObjectName(_fromUtf8("cifras"))
        self.horizontalLayout.addWidget(self.cifras)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.calcularButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calcularButton.setFont(font)
        self.calcularButton.setObjectName(_fromUtf8("calcularButton"))
        self.horizontalLayout_2.addWidget(self.calcularButton)
        self.helpButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.helpButton.setFont(font)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.horizontalLayout_2.addWidget(self.helpButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.iteraciones = QtGui.QTableView(self.centralwidget)
        self.iteraciones.setObjectName(_fromUtf8("iteraciones"))
        self.iteraciones.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.iteraciones, 2, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "El Bambaupa <3", None))
        self.label.setText(_translate("MainWindow", "F(X)=", None))
        self.label_2.setText(_translate("MainWindow", "A=", None))
        self.label_3.setText(_translate("MainWindow", "B=", None))
        self.label_4.setText(_translate("MainWindow", "Tolerancia=", None))
        self.tolerancia.setPlaceholderText(_translate("MainWindow", "0.005", None))
        self.label_6.setText(_translate("MainWindow", "Cifras=", None))
        self.calcularButton.setText(_translate("MainWindow", "Calcular", None))
        self.helpButton.setText(_translate("MainWindow", "Ayuda", None))
        self.label_5.setText(_translate("MainWindow", "Iteraciones", None))

