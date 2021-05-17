#Vamos a calcular el volumen de un cilindro partiendo del radio de base y la altura
from math import pi
print("Este programa sirve para calcular el volumen de un cilindro")

def run():
    radio_base=float(input("Por favor ingresa el radio de la base del cilindro: "))
    altura=float(input("Por favor ingresa la altura del cilindro: "))
    volumen_cilindro=(pi*(radio_base**2)*altura)
    print(f"El volumen del cilidro es {volumen_cilindro}")
        

if __name__=="__main__":
    run()
