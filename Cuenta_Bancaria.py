class CuentaBancaria:                        #Creación de clase con atributos uno público (titular) y (saldo sin guión bajo) 
    def __init__(self,titular,saldo):        #para validar al inicio de la cuenta en el setter
        self.titular= titular
        self.saldo= saldo

    @property                          #Creación de atributo de lectura y encapsulamiento con property y retorna el valor como 
    def saldo (self):                  #atributo privado
        return self._saldo
    @saldo.setter                    #Creación del setter que controla la validación de saldo que no puede ser negativo"
    def saldo(self,valor):
        if valor < 0:
            print ("El saldo no puede ser negativo")
        else:
            self._saldo=valor

    def depositar (self, monto):
        if not isinstance (monto, int):     #Validación para que el usuario utilice solo numeros y no str por ejemplo
            raise TypeError (f"el monto debe ser un número")  
        if monto <0:                     #IF para validar que el deposito sea positivo
            print("El valor a depositar no puede ser menor que 0")
        else:
            self.saldo+= monto   #si pasa las dos validaciones aumenta el saldo
        return self.saldo
    
    def retirar (self,monto): 
        if not isinstance (monto, int):     #Misma validación que se uso en depositar para que sea entero el monto a retirar
            raise TypeError (f"El monto debe ser un número")     
        if monto > self.saldo:      #IF para validar que hay fondos en la cuenta y que el monto sea positivo antes de sacar dinero
            print("Monto insuficiente")
        elif monto <=0:
            print("El monto a retirar debe ser mayor que 0")
        else:
            self.saldo-=monto

        return self.saldo

    #Instancias para probar funcionamiento
cuenta1= CuentaBancaria ("Juan", 2000)
cuenta1.depositar(500)
cuenta1.retirar(100)
cuenta1.retirar(4000) #Debe mostrar monto insuficiente

print (f"El saldo final de {cuenta1.titular} es {cuenta1.saldo}")






    
        

        
