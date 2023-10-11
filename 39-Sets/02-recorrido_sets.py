# =================================================
# Recorrido de Sets

# - los mismos fundamentos que con listas y tuplas
# =================================================

# ----------------------------------------------
# EJ:
conjunto = { 'X', 'Y', 100, -500, False }
# ----------------------------------------------

#? 1) Recorrido con for
print('\n1) Recorrido con for')

for elemento in conjunto:
    print(elemento)
# end for


#? 2) for + enumerate
print('\n3) for + enumerate')
# - con el enumerate podemos evitar el error
# - de tratar de acceder al índice

for index, elemento in enumerate(conjunto):
    print('Elemento #', index, '=', elemento)
# end for


#? 3) while no sería posible
print('\n4) while no sería posible')
# - recorrer un iterable con while
# - depende de un contador externo
# - para acceder a los elementos del iterable con un índice
# - pero recordemos que los sets no son accesibles con índice


# 3.1) Recordar while con lista
print('\n3.1) Recordar while con lista\n')

lista = ['A', 'B', 10, -8.9, True]

index = 0

while index < len(lista):
    print(lista[index])
    index += 1
# end while

# => como vemos es necesario el indexing cuando se recorre con while
# - el indexing no es posible con sets


# 3.2) Error al recorrer con while set
print('\n3.2) Error al recorrer con while set\n')

conjunto = { 'X', 'Y', 100, -500, False }

index = 0

while index < len(conjunto):
    #print( conjunto[index] ) #! TypeError: 'set' object is not subscriptable
    index += 1
# end while