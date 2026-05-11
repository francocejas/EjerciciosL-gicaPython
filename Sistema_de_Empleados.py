class Empleado:     #Creación de la clase empleado con atributos nombre y sueldo base
    def __init__(self,nombre,sueldobase):
        self.nombre= nombre
        self.sueldobase= sueldobase
    
    def Calcular_sueldo(self):   #Método calcular sueldo exclusivo de la clase padre
        return self.sueldobase
        

class Vendedor (Empleado):  #Creación de la clase hija empleado
    def __init__(self, nombre, sueldobase, comision):
        super() .__init__(nombre, sueldobase) #Herencia de la clase padre con sus atributos
        if comision <=0 or comision >=100:    #Validación de comisión de la clase hija
            print ("Comisión debe ser un porcentaje entre 0 y 100")
        else:
            self.comision= comision #asignación de porcentaje de la comisión si la validación fue exitosa
    def Calcular_sueldo(self): #sobreescritura del Método padre (calcular sueldo) con comisión exclusiva de clase hija
        sueldototal =(self.sueldobase + (self.sueldobase * self.comision/100)) 
        return sueldototal
    
#Instancia para probar funcionamiento
e=Empleado("Rodrigo", 10000)
totale= (e.Calcular_sueldo())
print(f"El sueldo total de un empleado es {totale}")


v=Vendedor("Esteban", 12000, 25)
totalv=(v.Calcular_sueldo())
print(f"El sueldo total de un vendedor es {totalv}")





    

    


       