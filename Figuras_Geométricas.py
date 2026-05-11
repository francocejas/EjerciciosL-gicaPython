from abc import ABC, abstractmethod

class Figura (ABC): 
    def obtener_area(self):  #Creación de clase abstracta. Todas las figuras estan obligadas a usar este método
        pass   

    def __add__(self,otro): #Sobrecarga de operador + para poder sumar áreas
        return (self.obtener_area() + otro.obtener_area())

class Cuadrado(Figura):  #Creación clase cuadrado que hereda de clase padre "Figura" y creación de atributo propio lado
    def __init__(self,lado):
        self.lado=lado
 
    def obtener_area(self): #Función heredada de clase padre (figura)
        return self.lado *self.lado
    
class Circulo(Figura):  #Creación de clase circulo que hereda de clase padre "Figura" y creación de atributo propio "radio"
    def __init__(self,radio):
        self.radio=radio
    
    def obtener_area(self):  #Función heredada de clase padre (Figura)
        return 3.14 * (self.radio**2)
    
def obtenercualquierarea(fig):  #función poliformica no le importa que figura es solo que tenga la función obtener_area
    print (fig.obtener_area())

#Instancia para probar funcionamiento
cua=Cuadrado(8)
cir=Circulo(3)

#Funcionamiento con lista 
figuras= [cua,cir]  
for f in figuras:
    obtenercualquierarea(f)  #Muestra el area de cualquier figura por la función poliformica

#Funcionamiento de suma de areas
suma= cua+cir

print (f"la suma de las figuras es {suma}") 

