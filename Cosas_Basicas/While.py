## CICLO WHILE EN PYTHON
## Tabla de Multiplicar en while
'''
numero = int(input("Ingresa el numero de la tabla:\n> "))
iterador = 1
while (iterador < 11):
    total = numero*iterador
    print(f"{numero} x {iterador} = {total}")
    iterador += 1
'''

## Raiz cuadrada de un numero
'''
import math
numero = int(input("Ingresa un numero \n>> "))
while (numero < 0):
    numero = int(input("Ingresa un numero positivo >:v \n>> "))
print(f"La raiz cuadrada de {numero} es: {math.sqrt(numero):.2}")
'''
## Conteo numeros par e impar
'''
cant = int(input("Ingresa la cantidad de numeros a contar: \n>> "))
iterador = 0
par = 0
impar = 0
while(iterador < cant):
    numero = int(input("Ingresa un numero: \n>> "))
    if(numero %2 == 0):
        par += 1
    else:
        impar += 1
    iterador += 1
print(f"Cantidad de numeros pares: {par}")
print(f"Cantidad de numeros impares: {impar}")
'''
## Conteo mayores y menores de edad
personas = int(input("Ingresa la cantidad de personas: \n>> "))
iterador = 0
mayores = 0
menores = 0
while(iterador < personas):
    edad = int(input("Ingresa la edad: \n>> "))
    if(edad>17):
        mayores += 1
    else:
        menores += 1
    iterador += 1
print(f"Mayores de edad: {mayores} \nMenores de edad: {menores} \n")