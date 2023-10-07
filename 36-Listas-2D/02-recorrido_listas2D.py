# ======================================
# Recorrido de Listas en 2 Dimensiones
# ======================================

#? 1) Recorrido de Lista 2D con Bucle Anidado for
print('\n1) Recorrido de Lista 2D con Bucle Anidado for')
# - en bucles anidados y su uso en recorrido de listas 2D o 3D
# - se puede usar la nomenclatura de los vectores unitarios para el recorrido
# - Recordar: Vectores Unitarios => i,j,k
# - En este caso:
#* i = filas
#* j = columnas

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz)
print()

for i in matriz:
    for j in i:
        print( j , end='   ')
    # end for
    print()
# end for


#? 2) Recorrido de Lista 2D con for + enumerate
print('\n2) Recorrido de Lista 2D con for + enumerate')

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz)
print()

for i, fila in enumerate(matriz):
    for j, columna in enumerate(fila):
        print( matriz[i][j] , end='   ' )
    # end for
    print()
# end for


#? 3) Recorrido de Lista 2D con while
print('\n3) Recorrido de Lista 2D con while')

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz)
print()

# con while, siempre contadores externos
i = 0 # filas
j = 0 # columnas

while i < len(matriz):
    while j < len(matriz[i]):
        print( matriz[i][j] , end='   ' )
        j += 1
    # end while
    j = 0
    i += 1
    print()
# end while



