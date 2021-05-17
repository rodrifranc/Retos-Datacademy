#Conversor de millas a kilometros y vicecersa

opcion=int("Bienvenido al conversor, elija la operacion que quiere realizar:\n1-Millas a kilometros\n2-Kilometros a millas")

while opcion>2 or opcion<1:
    print("Opcion incorrecta\nDebes elegir 1 si quieres convertir millas a kilometros\nDebes elegir 2 si quieres convertir kilometros a millas")


def milla_a_km():
    return milla*1.609344

def km_a_milla():
    return km/1.609344

if opcion==1:
    milla_a_km() 
elif opcion==2:
    km_a_milla()

