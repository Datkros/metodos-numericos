from sympy import *
from tabulate import tabulate

# Necesitarás descargar sympy y tabulate 

f = raw_input("Introduzca la funcion: ")
a0 = float(raw_input("Por favor ingrese el intervalo A: "))
b0 = float(raw_input("Por favor ingrese el intervalo B: "))
x = symbols('x')
f = sympify(f)


def encuentra_raiz(f,a0,b0,r,tolerancia=0.005, max_iter = 100):
    i = 0
    a = a0
    b = b0
    listaValores = [] 
    listaXr = []
    error = tolerancia
    fb = round(f.evalf(subs={x:b}),r)
    fa = round(f.evalf(subs={x:a}),r)
    print fb, fa
    if fb * fa < 0:
        while error >= tolerancia:
            fb = round(f.evalf(subs={x:b}),r)
            fa = round(f.evalf(subs={x:a}),r)
            xr = round(((a+b)/2.0),r)
            fxr = round(f.evalf(subs={x:xr}),r)
            listaXr.append(xr)
            if i > 0:
                error = abs((listaXr[i] - listaXr[i-1])/listaXr[i]) * 100
                #Almacenamos los valores en tuplas
                listaValores.append((i,a,b,fa,fxr,fa*fxr,error))
            else:
                listaValores.append((i,a,b,fa,fxr,fa*fxr,0))
            
            
            if fxr * fa < 0:
                b = xr
            else:
                a = xr

            i += 1
    else:
        print "No se puede realizar el metodo"

    row = []
    i = 0

    #Desempaquetamos los valores de las tuplas que se encuentran dentro de listaValores
    for i,a,b,fa,fxr,faxr,error in listaValores:
        values = []
        values.append(i)
        values.append('{0:.10f}'.format(i))
        values.append('{0:.10f}'.format(a))
        values.append('{:.9f}'.format(b))
        values.append('{:.9f}'.format(fa))
        values.append('{:.9f}'.format(fxr))
        values.append('{:.9f}'.format(faxr))
        values.append('{:.9f}'.format(error)+"%")
        row.append(values)
        i += 1
    print tabulate(row,['i','a','b','Xr','f(a)','f(Xr)','f(a)*f(Xr)','Ea'],tablefmt ='grid')

def __main__():
    encuentra_raiz(f,a0,b0,9)

if __name__ == __main__():
    __main__()