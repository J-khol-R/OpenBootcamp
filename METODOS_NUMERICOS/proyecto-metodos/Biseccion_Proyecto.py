from matplotlib import pyplot as plt
import numpy as np
from sympy import symbols
from sympy import lambdify
from sympy import sympify

print("")
x = symbols("x") #x es l variable simbolica que se usara en la funcion
fn = sympify(input("ingrese la funcion ")) #traduce la funcion de string para poder usarla y utiliza la variable simbolica
f = lambdify(x, fn) #evalua la funcion ingresada

#variables que vamos a usar en el metodo

a = float(input("ingrese el extremo inferior "))
b = float(input("ingrese el extremo superior "))
tolerancia = float(input("ingrese la tolerancia ")) #el limite de tolerancia
i = 0 #contador
ea = 1 #iniciar la variable de error
x_anterior = 0 #iniciar una variable de x anterior

#criterio inicial para verificar si la solucion esta en el intervalo seleccionado

if f(a)*f(b) < 0:
    print("")
    #titulo este centrado y que halla un total de 60 espacios, y el .format hace que python entienda lo que le envie
    print("{:^90}".format("METODO DE BISECCION"))
    print("{:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10}".format("i","a","f(a)","b","f(b)","xr","f(xr)","ea(%)"))

    while ea > tolerancia:
        xr = (a + b)/2
        ea = abs((xr - x_anterior)/xr)

        if f(xr)*f(a) < 0:
            b = xr
        else:
            a = xr

        
        x_anterior = xr

        print("{:^10} {:^10f}n{:^10f} {:^10f} {:^10f} {:^10f} {:^10f} {:^10}".format(i,a,f(a),b,f(b),xr,f(xr),round(ea*100,9)))
        i+=1

    print("")
    print("el valor de la raiz es",round(xr,9),"con un margen de error de ",round(ea*100,9),"%")


    #graficar la funcion y la raiz 
    xpts = np.linspace(-10,10) #me genera un vector con n numeros con los mismos espacios
    plt.plot (xpts, f(xpts)) #toma los numeros de los vectores y los evalua para graficarlos
    plt.title("Grafica de la funcion")
    plt.axhline(color="black") #lineas horizontales
    plt.axvline(color="black") #lineas verticales
    plt.scatter(xr,0,c="red") #pone el punto rojo en la raiz
    plt.annotate(round(xr,9),xy=(xr,0.5)) #que me muestre el valor de la raiz
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, which='both')
    plt.ylim([-15,15])
    plt.show()

else: #f(a)*f(b)>=0

    print("")
    print("la fincion no tiene una raiz en el intervalo de " + "x = " + str(a) + "a x = " + str(b))
    print("ingresar otra cota inferior y superior")

    xpts = np.linspace(-10,10)  #tamaño
    plt.plot(xpts, f(xpts))
    plt.title("grafica de la funcion") #titulo
    plt.axhline(color="black") #color de la linea
    plt.axvline(color="black") #color de la linea
    plt.xlabel("x") #nombre del eje x
    plt.ylabel("f(x)") #nombre del eje y
    plt.grid(True, which='both')
    plt.ylim([-15,15])
    plt.show()



