## CONDICIONALES EN PYTHON
##edad = int(input("Ingresa tu edad: \n"))
##if edad>17:
##    print("Es mayor de edad \n")
##else:
##    print("Es menor de edad \n")

##numero = int(input("Ingresa un numero: \n"))
##if(numero>0):
##    print("Es positivo \n")
##elif(numero<0):
##        print("Es negativo \n")
##else:
##    print("Es neutro \n")

## EJERCICIO 1
##n1 = int(input("Ingresa el primer numero: \n"))
##n2 = int(input("Ingresa el segundo numero: \n"))
##
##if(n1%2==0 and n2%2==0):
##    print("Ambos son pares \n")
##elif(n1%2==0 and n2%2!=0):
##    print(f"{n1} es par y {n2} no lo es")
##elif(n1%2!=0 and n2%2==0):
##    print(f"{n1} no es par y {n2} si lo es")
##else:
##    print("Ninguno es par \n")

## EJERCICIO 2
## Crear un numero que pida 3 numeros y determine cual es mayor
##A = float(input("Ingresa el primer numero: "))
##B = float(input("Ingresa el segundo numero: "))
##C = float(input("Ingresa el tercer numero: "))
##
##if (A>=B and A>=C):
##    print(f"{A} es mayor \n")
##elif(B>=A and B>=C):
##    print(f"{B} es mayor \n")
##elif(C>=A and C>=B):
##    print(f"{C} es mayor\n")

## EJERCICIO 3
## Crea un prgrama que compare dos nombres, y verificar si hay coincidencia o no, si es que ambos nombres comienzan con
## la misma letra  o si terminan con la misma letra.
##name1 = input("First name: ")
##name2 = input("Second name: ")
##
##if((name1[0] == name2[0]) or (name1[-1] == name2[-1])):
##    print(f"{name1} y {name2} empiezan y/o terminan con la misma letra \n")
##else:
##    print(f"No empiezan ni terminan con la misma letra \n")

## EJERCICIO 4
## Crear un programa que simule un cajero automatico con un saldo inicial de $2000, con el siguiente menu:
##  1. Ingreso de dinero
##  2. Retirar dinero
##  3. Mostrar dinero
##  4. Salir

inicial = 2000

op = int(input("Inserte su opcion:\n\t[1]: Ingresar\n\t[2]: Retirar\n\t[3]: Mostrar\n\t[4]: Salir\n> "))
if(op == 1):
    ingreso = float(input("Ingrese la cantidad a depositar: $"))
    inicial += ingreso
    print(f"Saldo Disponible: ${inicial} \n")

elif(op == 2):
    retiro = float(input("Ingrese la cantidad a retirar: $"))
    if(retiro>inicial):
        print("Saldo insuficiente :( \n")
    else:
        inicial -= retiro
        print(f"Saldo Disponible: ${inicial} \n")

elif(op == 3):
    print(f"Saldo Disponible: ${inicial} \n")
elif(op == 4):
    print("Gracias, vuelva pronto :D!!! \n")
else:
    print("Error al seleccionar las opciones XO!!!\n")
    