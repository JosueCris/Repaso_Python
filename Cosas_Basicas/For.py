## CICLOS FOR EN PYTHON
'''
array = [1, "Josue", 15.9, True, [17, 18]]
for i in array:
    print(f"Objeto: {i}")
'''

## EJERCICIO 1: CICLO FOR
## Crear un programa que muestre la sumatoria de tdos los numeros entre el 0 y el 100
## NOTA: rango 1, 2, 3,.... , 101 ->(nf-1) 
'''
suma = 0
for i in range(101):
    suma += i
    print(f"Sumando mas {i}: {suma}")
'''

## Tablas de Multiplicar en for
'''
numero = int(input("Ingresa un numero para la tabla: \n>> "))
for i in range(1, 11):
    total = numero*i
    print(f"{numero} x {i} = {total}")
'''
personas = int(input("Ingresa la cantidad de personas: \n>> "))
mayores = 0
menores = 0
for i in range(personas):
    edad = int(input("Ingresa tu edad: \n>> "))
    if(edad>17):
        mayores += 1
    else:
        menores += 1
print(f"Mayores de edad: {mayores} \nMenores de edad: {menores} \n")