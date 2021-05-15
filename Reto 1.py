#Este programa calculará el área de un trangulo dados la base y la altura

print("Vamos a calcular el area de un triangulo, por favor ingrese los datos: ")


base=float(input("Ingrese la base en metros: "))
altura=float(input("Ingrese la altura en metros: "))


while base<=0 or altura<=0:
    print("Por favor ingrese valores correctos: ")
    base=float(input("Ingrese la base en metros: "))
    altura=float(input("Ingrese la altura en metros: ")) 

area=(base*altura)/2
print(f"El area del triangulos es {area} metros cuadrados")