#Programa basado en el juego de piedra, papel o tijera, el usuario podrá elegir también si quiere que el ganador sea 2 de 3 o simple
from random import randint
import random

modo_juego=int(input("Bienvenido al juego piedra, papel o tijera. Elija el modo de juego>\n1-Simple\n2-Dos de tres\nRespuesta: "))

while modo_juego>2 or modo_juego<=0:
    print("Por favor elija el modo de juego segun las opciones dadas: ")
    modo_juego=int(input("1-Simple\n2-Dos de tres\nRespuesta: "))

def modo_simple():
    usuario=int(input("Ingrese una opcion:\n1-Piedra\n2-Papel\n3-Tijera\n"))
    maquina= random.randint(1,3)

    if maquina==1:
        aux="Piedra"
    elif maquina==2:
        aux="Papel"
    else:
        aux="Tijera"

    if maquina==1 and usuario==3 or maquina==3 and usuario==2 or maquina==2 and usuario==1:
        print(f"Lo siento perdiste :C\nLa maquina eligio {aux}")
    elif maquina==3 and usuario==1 or maquina==2 and usuario==3 or maquina==1 and usuario==2:
        print(f"Ganaste!! :D\nLa maquina eligio {aux}")
    else:
        print("Es un empate!!\nLa maquina tambien eligio {aux}"")

if modo_juego==1:
    modo_simple()
else:
    modo_dostres()


