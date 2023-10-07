# ============================================================
# Listas en 2 Dimensiones

# - Una lista en Python contiene todo tipo de elementos
# - Incluso una misma lista
# - Las listas en 2D pueden simular a las matrices numéricas
# ============================================================

#? 1) Recordar: Listas en Python pueden todo tipo de elementos
print('\n1) Recordar: Listas en Python pueden todo tipo de elementos')

lista = ['Sebas', 10, True, 5.5, [100,200,300]]

print( lista , type(lista), len(lista) )

# - accediendo por índices
print()
print( lista[0] , type(lista[0]) )
print( lista[1] , type(lista[1]) )
print( lista[2] , type(lista[2]) )
print( lista[3] , type(lista[3]) )
print( lista[4] , type(lista[4]) )

# - y en el último elemento podemos acceder a sus índices también
# - aquí utilizamos la nomenclatura del doble corchete
print()
print( lista[4][0] , type(lista[4][0]) )
print( lista[4][1] , type(lista[4][1]) )
print( lista[4][2] , type(lista[4][2]) )


#? 2) Listas en 2D => Simulan Matrices Numéricas
print('\n2) Listas en 2D => Simulan Matrices Numéricas')

# ej:
'''
1   2   3
4   5   6
7   8   9
'''

matriz = [[1,2,3] , [4,5,6] , [7,8,9]]
print(matriz, len(matriz))

# - podemos mejorar su representación en el script
# - de esta manera observamos más claramente
#   => número de filas
#   => número de columnas

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz)
print('--------------------')
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('--------------------')
print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])
print('--------------------')
print(matriz[1][0])
print(matriz[1][1])
print(matriz[1][2])
print('--------------------')
print(matriz[2][0])
print(matriz[2][1])
print(matriz[2][2])

# => por tanto, se podría recorrer esto con bucle anidado