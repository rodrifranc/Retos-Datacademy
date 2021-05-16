#Este programa calculará el área de un trangulo dados la base y la altura
from math import sqrt
print("Vamos a calcular el area de un triangulo, por favor ingrese los datos: ")


base=float(input("Ingrese la base en metros: "))
altura=float(input("Ingrese la altura en metros: "))


while base<=0 or altura<=0:
    print("Por favor ingrese valores correctos: ")
    base=float(input("Ingrese la base en metros: "))
    altura=float(input("Ingrese la altura en metros: ")) 

area=(base*altura)/2
print(f"El area del triangulo es {area} metros cuadrados")

#Calcularemos si el triangulo es isósceles, equilatero o escaleno

c1=(base/2)^2
c2=altura^2
def isosceles(self, a):
    if c1+c2==a^2:
        print("El triangulo es isosceles!!")
    else:
        print("El triangulo es Escaleno!!")


if (base^2)==((base/2)^2)+(altura^2):
    print("El triangulo es equilatero!!")
else:
    print("El triangulo no es equilatero, por favor ingrese la longitud de uno de los lados: \n ")
    lado_1=float(input("Lado 1: "))
    isosceles(lado_1)