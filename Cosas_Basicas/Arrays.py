## ARREGLOS (VECTORES Y MATRICES) EN PYTHON
array = [1, "Josue", 15.9, True, [15.9, 17, 18]]
##print(array[-1:3]) ## No sale nada
##print(len(array) ## Calcula el tamaño del arreglo
##print(len(array[1:-2])) ## Lo mismo de arriba pero con rango
##
##array.append("Tellez") ## Agrega al final del arreglo
##array.insert(4, False) ## Agrega en cualquier posicion del arreglo
##array.extend([1, 'H', 2.5]) ## Agrega mas de un elemento al final del arreglo
##print(array)
##print("Josue" in array) ## Buscamos un elemento en el arreglo
##print(f"El elemento {array[2]} se encuentra en la posicion [{array.index(15.9)}]") ## Me dice en que posicion se encuentra el elemento que especifico
##print(f"El elemento Josue se repite {array.count('Josue')} veces") ## Cuenta las veces que se repite un elemento 
##NOTA: Si se va a concatenar la funcion con frases asegurarse que si hay se contara cadenas se debe encerrar en apostrofe ('') de lo contraio encerrarlo con comillas ("")
##array.reverse() ## Invierte las posiciones del arreglo
##print(array)
##print(array.remove("Josue") ## Elimina el elemento del arreglo
##print(array)
array.clear() ## Hace limpieza completa del arreglo
##print(array)

arreglo1 = [3, 1, 2]
arreglo2 = [5, 4, 6]
arreglo3 = arreglo1+arreglo2
print(arreglo3) ## Concatenamos el arreglo 1 y 2 en uno solo
arreglo3.sort() ## Ordena de menor a mayor el arreglo solo si se trata de enteros o flotantes (cadenas o booleanos manda error)
print(arreglo3)
arreglo3.sort(reverse=True) ## En este caso ordena de mayor a menor (cadenas o booleanos manda error)
print(arreglo3)
