## CONJUNTOS EN PYTHON (SEGUNDO PARCIAL DE MATE DISCRETAS xD)
A = {1, 2, 3, 4}
B = {2, 3, 5, 6}
C = {3, 4, 6, 7}
U = A | B | C
##print(A == B) ## Comparación
##print(f"Union de A y B: {A | B}") ## Union
##print(f"Union de A y C: {A | C}")
##print(f"Union de B y C: {B | C}")
##print(f"Interseccion de A con B: {A & B}") ## Interseccion
##print(f"Interseccion de A con C: {A & C}")
##print(f"Interseccion de B con C: {B & C}")
print(f"Universo: {U}")
print(f"Todo lo que hay en A que no hay en B: {A-B}")
print(f"Todo lo que hay en A que no hay en C: {A-C}")
print(f"Todo lo que hay en B que no hay en A: {B-A}")
print(f"Todo lo que hay en B que no hay en C: {B-C}")
print(f"Todo lo que hay en C que no hay en A: {C-A}")
print(f"Todo lo que hay en C que no hay en B: {C-B}")
print(f"Diferencia simetrica de A y B: {A ^ B}") ## Diferencia simetrica (La union de la diferencia de ambos conjuntos)
print(f"Diferencia simetrica de A y C: {A ^ C}")
print(f"Diferencia simetrica de B y C: {B ^ C}")