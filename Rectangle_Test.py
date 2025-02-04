techo= []
panel= []
areaTecho = int
areaPaneles = int
resultado = int

panel.append(input("Ingrese las medidas de los paneles\nPrimer Lado: "))
panel.append(input("Segundo Lado: "))

techo.append(input("Ingrese las medidas del techo\nPrimer Lado: "))
techo.append(input("Segundo Lado: "))

def paneles_solares(panel,techo):
    if(int(techo[0])<int(panel[0]) and int(techo[0])< int(panel[1]) ):
        resultado = 0
        return(print("El resultado es:",resultado,"ya que no hay espacio suficiente"))
    if(int(techo[1])<int(techo[0]) and int(techo[1])< int(panel[1]) ):
        resultado = 0
        return(print("El resultado es:",resultado,"ya que no hay espacio suficiente"))
    
    areaTecho = int(techo[0])*int(techo[1])
    areaPaneles = int(panel[0])*int(panel[1])

    resultado = areaTecho/areaPaneles
    return(print("En el techo ingresado hay espacio para",int(resultado),"paneles"))


paneles_solares(panel,techo)



