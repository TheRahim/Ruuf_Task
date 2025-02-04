import math

techo= []
panel= []
areaTecho = int
areaPaneles = int
resultado = int
x= int

x=input("Si el techo tiene forma de triangulo isoceles,ingrese 1\nSi el techo tiene forma de rectangulo,ingrese 0\n")

panel.append(input("Ingrese las medidas de los paneles\nPrimer Lado: "))
panel.append(input("Segundo Lado: "))

if (int(x)==1):
    techo.append(input("Ingrese las medidas del techo\nLado Base: "))
    techo.append(input("Lados Laterales: "))
else:
    techo.append(input("Ingrese las medidas del techo\nPrimer Lado: "))
    techo.append(input("Segundo Lado: "))

def paneles_solares(panel,techo,x):
    if(int(techo[0])<int(panel[0]) and int(techo[0])< int(panel[1]) ):
        resultado = 0
        return(print("El resultado es:",resultado,"ya que no hay espacio suficiente"))
    if(int(techo[1])<int(techo[0]) and int(techo[1])< int(panel[1]) ):
        resultado = 0
        return(print("El resultado es:",resultado,"ya que no hay espacio suficiente"))
    if(int(x)==1):
        h=(int(techo[1])*int(techo[1]))-((int(techo[0])/2)*(int(techo[0])/2))
        h= math.sqrt(h)

        areaTecho = (int(techo[0])* h)/2
        areaPaneles = int(panel[0])*int(panel[1])

        resultado = areaTecho/areaPaneles
    else:
        areaTecho = int(techo[0])*int(techo[1])
        areaPaneles = int(panel[0])*int(panel[1])

        resultado = areaTecho/areaPaneles
    
    return(print("En el techo ingresado hay espacio para",int(resultado),"paneles"))


paneles_solares(panel,techo,x)





