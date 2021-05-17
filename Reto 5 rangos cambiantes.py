#Juego de comparacion de numeros
import os

print("Bienvenido al juego de comparacion de numeros, en este juego ingresaras dos numeros y luego un tercer numero el cual debera estar en el rango de los dos primeros")
clear=os.system("cls")
def run():
    n1=int(input("Por favor ingresa el primer numero: "))
    n2=int(input("Por favor ingresa el segundo numero: "))
    while n1==n2 or n1==n2+1 or n2==n1+1:
        print("Los numeros no deben ser iguales o consecutivos")
        n1=int(input("Por favor ingresa el primer numero: "))
        n2=int(input("Por favor ingresa el segundo numero: "))
    
    clear
    n3=int(input("Ingresa el numero de comparacion: "))

    if n1>n2:
        upper=n1
        lower=n2
    elif n2>n1:
        upper=n2
        lower=n1

    if n3>upper:
        print("El numero debe ser menor")
        n3=int(input("Ingresa el numero de comparacion: "))
    elif n3<lower:
        print("El numero debe ser mayor")
        n3=int(input("Ingresa el numero de comparacion: "))
    else:
        print(f"Ya estas en el rango de {n1} y {n2}")
        


if __name__=="__main__":
    run()