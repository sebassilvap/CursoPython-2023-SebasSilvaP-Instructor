# =======================================================
# Listas en 3 Dimensiones

# - De manera sencilla se pueden definir
# - Como una lista que contiene listas en 2 dimensiones
# - Lo vamos a ver mejor en la práctica
# =======================================================


#? 1) Recordar: Lista 2D
print('\n1) Recordar: Lista 2D')

# => ejemplo básico de lista en 2D ó matriz 2x2

matriz = [
    ['a', 'b'],
    ['c', 'd']
]

print(matriz)

# =>  a partir de esto construimos una lista en 3D

lista3D = [
    [ ['a','b'] , ['c','d'] ],
    [ ['e','f'] , ['g','h'] ],
    [ ['i','j'] , ['k','l'] ],
]

print(lista3D)

# => por facilidad de comprensión
# - se podría crear con variables

lista2D_1 = [ ['a','b'] , ['c','d'] ]
lista2D_2 = [ ['e','f'] , ['g','h'] ]
lista2D_3 = [ ['i','j'] , ['k','l'] ]

# => de esta manera

lista3D = [
    lista2D_1,
    lista2D_2,
    lista2D_3
]

print(lista3D)