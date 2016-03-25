# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ayuda.ui'
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

class Ui_ayudawindow(object):
    def setupUi(self, ayudawindow):
        ayudawindow.setObjectName(_fromUtf8("ayudawindow"))
        ayudawindow.resize(435, 311)
        self.gridLayout = QtGui.QGridLayout(ayudawindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ayuda = QtGui.QLabel(ayudawindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ayuda.setFont(font)
        self.ayuda.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ayuda.setTextFormat(QtCore.Qt.LogText)
        self.ayuda.setWordWrap(True)
        self.ayuda.setObjectName(_fromUtf8("ayuda"))
        self.gridLayout.addWidget(self.ayuda, 0, 0, 1, 2)
        self.label_7 = QtGui.QLabel(ayudawindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(ayudawindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(ayudawindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(ayudawindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label = QtGui.QLabel(ayudawindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_9 = QtGui.QLabel(ayudawindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ayudawindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_8 = QtGui.QLabel(ayudawindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)

        self.retranslateUi(ayudawindow)
        QtCore.QMetaObject.connectSlotsByName(ayudawindow)

    def retranslateUi(self, ayudawindow):
        ayudawindow.setWindowTitle(_translate("ayudawindow", "Ayuda", None))
        self.ayuda.setText(_translate("ayudawindow", "Las funciones en el cuadro F(X) deben cumplir con la siguiente sintaxis:", None))
        self.label_7.setText(_translate("ayudawindow", "Potenciacion", None))
        self.label_5.setText(_translate("ayudawindow", "Multiplicacion", None))
        self.label_6.setText(_translate("ayudawindow", "(e^x)     ->     (E**x)", None))
        self.label_4.setText(_translate("ayudawindow", "x      ->     *", None))
        self.label.setText(_translate("ayudawindow", "Exponencial", None))
        self.label_9.setText(_translate("ayudawindow", "Division", None))
        self.label_3.setText(_translate("ayudawindow", "(e)     ->     (E)", None))
        self.label_8.setText(_translate("ayudawindow", "÷     ->     /", None))

