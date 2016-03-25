from sympy import *
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from falsa_ui import Ui_MainWindow
from ayuda_ui import Ui_ayudawindow

x = symbols('x')

class Ayuda(QDialog):

    def __init__(self,*args):
        QDialog.__init__(self,*args)

        self.ayuda = Ui_ayudawindow()
        self.ayuda.setupUi(self)

class MainWindow(QMainWindow):
    
    def __init__(self,*args):
        QMainWindow.__init__(self,*args)

        self.ui_window = Ui_MainWindow()
        self.ui_window.setupUi(self)
        self.ui_window.calcularButton.clicked.connect(self.calcular)
        self.ui_window.helpButton.clicked.connect(self.mostrarayuda)
        self.ui_window.tolerancia.setToolTip("Si no se especifica ningun valor para la tolerancia, se tomara 0.005 por defecto")
        self.ui_window.cifras.setToolTip("Si no se especifica ningun valor para las cifras significativas se tomara 9 por defecto")
        
    def mostrarayuda(self):
        self.w = Ayuda()
        self.w.show()
        
    def calcular(self):
        f = sympify(str(self.ui_window.funcion.text()))
        a0 = float(self.ui_window.a.text())
        b0 = float(self.ui_window.b.text())
        r = self.ui_window.cifras.text()
        tolerancia = self.ui_window.tolerancia.text()
        if r == "" and tolerancia == "":
            self.encuentra_raiz(f,a0,b0)
        elif r != "" and tolerancia == "":
            r = int(r)
            self.encuentra_raiz(f,a0,b0,r)
        elif r == "" and tolerancia != "":
            tolerancia = float(tolerancia)
            self.encuentra_raiz(f,a0,b0,tolerancia=tolerancia)
        

    def encuentra_raiz(self,f,a0,b0,r=9,tolerancia=0.005, max_iter = 100):
        i = 0
        a = a0
        b = b0
        listaValores = []
        listaXr = []
        error = tolerancia
        while error >= tolerancia:
            fb = round(f.evalf(subs={x:b}),r)
            fa = round(f.evalf(subs={x:a}),r)
            xr = round(b - ((fb * (a-b))/(fa - fb)),r)
            listaXr.append(xr)
            fxr = round(f.evalf(subs={x:xr}),r)
            if i > 0:
                error = abs((listaXr[i] - listaXr[i-1])/listaXr[i]) * 100
                listaValores.append((i,a,b,fa,fb,xr,fxr,fa*fxr,error))
            else:
                listaValores.append((i,a,b,fa,fb,xr,fxr,fa*fxr,0))
            if fxr * fa < 0:
                b = xr
            else:
                a = xr
            i += 1

        modelo = self.setModel(listaValores)
        modelo.setHorizontalHeaderLabels(['Iteracion','a','b','fa','fb','xr','fxr','F(a)*F(xr)','Error'])
        self.ui_window.iteraciones.setModel(modelo)

    def setModel(self,lista):
        model = QtGui.QStandardItemModel(parent=self)
        for elemento in lista:
            listaItems = []
            for x in elemento:
                item = QtGui.QStandardItem(str(x))
                listaItems.append(item)
            model.appendRow(listaItems)
        return model
    
class App(QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = MainWindow()
        self.main.setAttribute(Qt.WA_DeleteOnClose)
        self.connect(self, SIGNAL("lastWindowClosed()"), self.cierra)
        self.main.show()

    def cierra(self):
        self.exit(0)

def main(args):
    global app
    app = App(args)
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)
