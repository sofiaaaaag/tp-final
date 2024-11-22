###ejercicio 1
""" class Empleado:
    def __init__(self, _nombre="" , _salario="" , _años_antiguedad=""):
        self.nombre = _nombre
        self.salario = _salario
        self.años_antiguedad = _años_antiguedad
    def calcular_bono (self):
            bono = self.años_antiguedad * self.salario * 0.05
            print(f"El bono para {empleado.nombre} es: {bono}")
empleado  = Empleado ( _nombre = "pepe", _salario=50 , _años_antiguedad=2 )
empleado.calcular_bono() """

###ejercicio 2 
""" import datetime
fechaActual = datetime.date.today()
diaDelta = datetime.timedelta(days=5)
fechaFutura = fechaActual=diaDelta

class Producto:
     def __init__(self, _nombre="" , _precio= 0, _fecha =""):
          self.nombre = _nombre
          self.precio = _precio
          self.fecha = _fecha
     def aplicar_descuento (self):
          descuento = self.precio * 0.90
          return descuento
class ProductoPerecedero(Producto):
     def __init__(self, _nombre="" , _precio="", _fecha = ""):
          self.nombre = _nombre
          self.precio = _precio
          self.fecha= _fecha
     def aplicar_descuento (self):
         if fechaFutura == fechaFutura:
              descuento = self.precio * 0.80
              print(f"El precio de {self.nombre} con descuento es: {descuento}")
productoperecedero = ProductoPerecedero ( " fideos", 500,  fechaActual)
productoperecedero.aplicar_descuento() """

###ejercicio 3 (en este punto no entendí a que se referia con mostrar el tiempo de uso desde que arrancó, asi que lo deje asi)
""" from abc import ABC, abstractmethod
class coche(ABC):
     @abstractmethod
     def arrancar(self):
          pass
     @abstractmethod
     def detener(self):
          pass
class arrancar (coche):
     def arrancar(self):
          return "El coche arranco"
     def detener(self):
          return "El coche se detuvo"
arrancar = arrancar()
print (arrancar.arrancar())
print (arrancar.detener())
class bicicleta(ABC):
     @abstractmethod
     def arrancar(self):
          pass
     @abstractmethod
     def detener(self):
          pass
class arrancar (bicicleta):
     def arrancar(self):
          return "La bicicleta esta andando"
     def detener(self):
          return "La bicicleta se detuvo"
arrancar = arrancar()
print (arrancar.arrancar())
print (arrancar.detener())
 """
 ### ejercicio 4
""" class Cliente:
     def __init__(self, _nombre="" , _correo="", _saldo= ""):
          self.nombre = _nombre
          self.correo = _correo
          self.tipo_cliente =  "premium" if _saldo >= 1000 else "regular"
          self.saldo = _saldo
     def actualizar_saldo(self, saldo_actuaizado):
          saldo_actualizado = self.saldo
          print (f"El saldo de {self.nombre} corresponde a tipo: {self.tipo_cliente}")
cliente = Cliente (_nombre = "pepe" , _correo= "pepe@gmail.com", _saldo= 900 )

cliente.actualizar_saldo(900) """
### ejercicio 5
""" from math_utils import calcular_division_segura 

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

calcular_division_segura(num1 , num2)
res = calcular_division_segura(num1, num2)
print (f"El resultado de tu division es: {res}") """
### ejercicio 6 
""" lista = [1,2,3,4,5,6,7,8,9,10]
def procesar_lista_numeros(lista:list):
        
     lista_pares = []
     for numero in lista:
      if numero % 2==0:
          
          lista_pares.append(numero)
     return lista_pares

procesar_lista_numeros (lista) 
print (procesar_lista_numeros(lista))
     """
### ejercicio 8
# El tipado de funciones sirve para especificar los tipos de datos que van a ser los parametros de esa funcion. para mi es importante para que el código sea mas legible y entendible.
""" Ejemplo con enteros:
def calcular_division_segura (a: int, b: int)-> int:
return a / b """
"""ejemplo con string:
def saludar (nombre: str)-> str:
print (f"hola {nombre}")
 """



    
    


     




    
     

