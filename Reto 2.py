#Programa basado en el juego de piedra, papel o tijera, el usuario podrá elegir también si quiere que el ganador sea 2 de 3 o simple

modo_juego=int(input("Bienvenido al juego piedra, papel o tijera. Elija el modo de juego>\n1-Simple\n2-Dos de tres\nRespuesta: "))

while modo_juego>2 or modo_juego<=0:
    print("Por favor elija el modo de juego segun las opciones dadas: ")
    modo_juego=int(input("1-Simple\n2-Dos de tres\nRespuesta: "))