###ejercicio 7
from dolar import convertir_a_peso
from dolar import convertir_a_dolar
from euro import convertir_a_euro
from euro import convertir_a_pesos
menu = input("Elija que tipo de conversion desea realizar (convertir_a_peso, convertir_a_dolar, convertir_a_euro, convertir_a_pesos): ")
eleccion =""
if menu == "convertir_a_peso":
    valor_dolar = int(input("Ingrese el valor en dolares para realizar la conversion:"))
    convertir_a_peso (valor_dolar)
    res = convertir_a_peso (valor_dolar)
    print (f"El resultado de tu conversion es : {res} pesos")
elif menu == "convertir_a_dolar":
    valor_peso = int(input ("Ingrese el valor en pesos para realizar la conversion:"))
    convertir_a_dolar (valor_peso)
    res = convertir_a_dolar(valor_peso)
    print (f"El resultado de tu conversion es : {res} dolares")
elif menu == "convertir_a_euro":
    valor_peso = int(input("Ingrese el vlor en pesos para realizar la conversion:"))
    convertir_a_euro (valor_peso)
    res = convertir_a_euro(valor_peso)
    print (f"El resultado de tu conversion es: {res} euros")
elif menu == "convertir_a_pesos":
    valor_euro = int(input("Ingrese el valor en euros para realizar la conversion:"))
    convertir_a_pesos(valor_euro)
    res= convertir_a_pesos(valor_euro)
    print (f"El resultado de tu conversion es: {res} pesos")