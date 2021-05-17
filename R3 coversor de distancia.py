#Conversor de millas a kilometros y vicecersa

opcion=int(input("Bienvenido al conversor, elija la operacion que quiere realizar:\n1-Millas a kilometros\n2-Kilometros a millas:\n"))

while opcion>2 or opcion<1:
    print("Opcion incorrecta\nDebes elegir 1 si quieres convertir millas a kilometros\nDebes elegir 2 si quieres convertir kilometros a millas")
    opcion=int(input("Elija la operacion que quiere realizar:\n1-Millas a kilometros\n2-Kilometros a millas:\n"))

def milla_a_km():
    milla=float(input("Ingrese cantidad de millas: "))
    kilometros=milla*1.609344
    print(f"{milla} millas equivale a {kilometros} kilometros")

def km_a_milla():
    km=float(input("Ingrese cantidad de kilometros: "))
    millas= km/1.609344
    print(f"{km} kilometros equivale a {millas} millas")


if opcion==1:
    milla_a_km()
elif opcion==2:
    km_a_milla()

