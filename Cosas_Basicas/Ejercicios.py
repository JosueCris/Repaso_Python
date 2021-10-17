## EJERCICIO 1
##a = float(input("Ingresa el valor de a:\n"))
##b = float(input("Ingresa el valor de b:\n"))
##c = float(input("Ingresa el valor de c:\n"))
##form = ((c+5)*(b**2-3*a*c)*a**2)/(4*a)
##print("El resultado es:", form)

## EJERCICIO 2
##a = float(input("Ingresa el valor de a: \n"))
##b = float(input("Ingresa el valor de b: \n"))
##
##a, b = b, a
##
##print("a =",a, "\nb =", b)
##print()
##print("a =",b, "\nb =", a)

## EJERCICIO 3
##import math
##radio = float(input("Ingresa el radio del circulo: \n"))
##area = math.pi*radio**2
##longitud = 2*math.pi*radio
##print(f"Area del circulo: {area:.2f}")
##print(f"Longitud del circulo: {longitud:.2f}")

## EJERCICIOS 4
## Obtener el precio final que se tiene que pagar si se aplica el 36% de descuento del total de la compra
precio = float(input("Precio inicial: $"))
porcentaje = float(input("Ingresa el porcentaje de descuento: "))
descuento = precio*(porcentaje/100)
total = precio-descuento
print(f"Descuento: ${descuento:.2f}")
print(f"Precio con descuento: ${total:.2f}")
