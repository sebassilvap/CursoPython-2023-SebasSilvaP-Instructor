# ================================================================
# Recorrido de listas en 3 Dimensiones

# - Una convención como se dijo anteriormente
# - Es utilizar la nomenclatura de los vectores unitarios
# - Otra manera de verlo es como si se tratase de un cubo rubix

'''
i - ancho
j - alto
z - profundidad
'''

# - listas 2D => enlace entre la programación y gráficos 2D
# - listas 3D => enlace entre la programación y gráficos 3D
# ================================================================


#? 1) Ejemplo Básico de Lista en 3D
print('\n1) Ejemplo Básico de Lista en 3D')

lista3D = [
    [ ['a','b'] , ['c','d'] ],
    [ ['e','f'] , ['g','h'] ],
    [ ['i','j'] , ['k','l'] ],
]

# => construcción paso a paso

lista2D_1 = [ ['a','b'] , ['c','d'] ]
lista2D_2 = [ ['e','f'] , ['g','h'] ]
lista2D_3 = [ ['i','j'] , ['k','l'] ]

lista3D = [
    lista2D_1,
    lista2D_2,
    lista2D_3
]

print( lista3D )



#? 2) Recorrido Básico de Lista 3D con for
print('\n2) Recorrido de Lista 3D con for')

lista3D = [
    [ ['a','b'] , ['c','d'] ],
    [ ['e','f'] , ['g','h'] ],
    [ ['i','j'] , ['k','l'] ],
]

print( lista3D )

for i in lista3D:
    for j in i:
        for k in j:
            print(k)
# end for

print('\n----------------------------\n')

for i in lista3D:
    for j in i:
        for k in j:
            print(k , end='  ')
        # end for
        print()
# end for

print('\n----------------------------\n')

for i in lista3D:
    for j in i:
        for k in j:
            print(k , end='  ')
        # end for
        print()
    # end for
    print()
# end for



#? 3) Recorrido Básico de Lista 3D con for + enumerate
print('\n3) Recorrido Básico de Lista 3D con for + enumerate')

lista3D = [
    [ ['a','b'] , ['c','d'] ],
    [ ['e','f'] , ['g','h'] ],
    [ ['i','j'] , ['k','l'] ],
]

print( lista3D )

# utilizando la comparación a un cubo rubix:

print()

for i, ancho in enumerate(lista3D):
    for j, alto in enumerate(ancho):
        for k, produndidad in enumerate(alto):
            print( lista3D[i][j][k] , end='  ' )
        # end for
        print()
    # end for
    print()
# end for



#? 4) Recorrido Básico de Lista 3D con while
print('\n4) Recorrido Básico de Lista 3D con while')

lista3D = [
    [ ['a','b'] , ['c','d'] ],
    [ ['e','f'] , ['g','h'] ],
    [ ['i','j'] , ['k','l'] ],
]

print( lista3D )

print()

# contadores del while - vectores unitarios
i = 0
j = 0
k = 0

while i < len( lista3D ):
    while j < len( lista3D[i] ):
        while k < len( lista3D[i][j] ):
            print( lista3D[i][j][k] , end='  ' )
            k += 1
        # end while
        print()
        j += 1
        k = 0
    # end while
    print()
    i += 1
    j = 0
# end while