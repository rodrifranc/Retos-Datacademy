#Programa basado en el juego de piedra, papel o tijera, el usuario podrá elegir también si quiere que el ganador sea 2 de 3 o simple
from random import randint
import os#Con esta libreria podemos limpiar la pantalla

modo_juego=int(input("Bienvenido al juego piedra, papel o tijera. Elija el modo de juego>\n1-Simple\n2-Dos de tres\nRespuesta: "))
clear=os.system("cls")



while modo_juego>2 or modo_juego<=0:
    print("Por favor elija el modo de juego segun las opciones dadas: ")
    modo_juego=int(input("1-Simple\n2-Dos de tres\nRespuesta: "))


def modo_simple():
    usuario=int(input("Ingrese una opcion:\n1-Piedra\n2-Papel\n3-Tijera\n"))
    maquina= randint(1,3)

    if maquina==1:
        aux="Piedra"
    elif maquina==2:
        aux="Papel"
    else:
        aux="Tijera"
    clear
    if maquina==1 and usuario==3 or maquina==3 and usuario==2 or maquina==2 and usuario==1:
        print(f"Lo siento perdiste :C\nLa maquina eligio {aux}")
        return 0
    elif maquina==3 and usuario==1 or maquina==2 and usuario==3 or maquina==1 and usuario==2:
        print(f"Ganaste!! :D\nLa maquina eligio {aux}")
        return 1
    else:
        print(f"Es un empate!!\nLa maquina tambien eligio {aux}")


def modo_dostres():
    c1=0
    c2=0
    modo_simple()
    if modo_simple==0:
        print("La maquina gano esta ronda, suerte la proxima")
        c1+=1
    else:
        print("Ganaste esta ronda, sigue asi :D")
        c2+=1
    modo_simple()
    if modo_simple==0:
        print("La maquina gano esta ronda, suerte la proxima")
        c1+=1
    else:
        print("Ganaste esta ronda, sigue asi :D")
        c2+=1
    modo_simple()
    if modo_simple==0:
        print("La maquina gano esta ronda, suerte la proxima")
        c1+=1
    else:
        print("Ganaste esta ronda, sigue asi :D")
        c2+=1

    if c1>c2:
        print(f"Lo siento, la maquina gano {c1} de 3")
    elif c2>c1:
        print(f"Muy bien, ganaste {c2} de 3")
    else:
        print("Es un empate!!")

if modo_juego==1:
    modo_simple()
else:
    modo_dostres()


