# =================================================================
# RECORDAR: Packing & Unpacking de Tuplas

# - recordatorio del tema de tuplas
# - operación de packing y unpacking
# - unpacking con *

#   https://www.w3schools.com/python/python_tuples_unpack.asp
# =================================================================


#? 1) Recordar "packing" & "unpacking" de tuplas
print('\n1) Recordar "packing" & "unpacking" de tuplas')

# -------------------------------------
# 1.1) packing de tuplas
print('\n1.1) unpacking de tuplas\n')
# -------------------------------------
# - no es más que el proceso de creación de una tupla
# - cuando creamos una tupla asignamos valores a esta
# - recordar, valores no modificables
# - esa es su diferencia de listas

heroes = ('goku', 'superman', 'ironman')
villanos = tuple( ('freezer', 'lex luthor', 'thanos') )

print( heroes, type(heroes), len(heroes) )
print( villanos, type(villanos), len(villanos) )


# -------------------------------------
# 1.2) unpacking de tuplas
print('\n1.2) unpacking de tuplas\n')
# -------------------------------------
# - es el proceso de extraer los valores de una tupla
# - y asignarlos a variables
# - IMPORTANTE: el número de variables = número de valores en tupla

(h1, h2, h3) = heroes
(v1, v2, v3) = villanos

print(h1, h2, h3)
print(v1, v2, v3)



#? 2) Recordar: "unpacking" + *
print('\n2) Recordar: "unpacking" + *')
# - de esta manera podemos asignar menos variables
# - que valores de tupla
# - al momento del unpacking
# - la variable con asterisco guarda el resto en forma de lista

animales = ('perro', 'gato', 'loro', 'colibrí', 'paloma')

#(can, felino, aves) = animales
#! ValueError: too many values to unpack (expected 3)

(can, felino, *aves) = animales

print( can, type(can) )
print( felino, type(felino) )
print( aves, type(aves) )



#? 3) Recordar: Podíamos tener la variable con * en penúltima posición
print('\n3) Recordar: Podíamos tener la variable con * en penúltima posición')

personajes = ('goku', 'krilin', 'broly', 'freezer', 'buu', 'gohan')

(h1, h2, *villanos, h3) = personajes

print( h1, type(h1) )
print( h2, type(h2) )
print( h3, type(h3) )
print( villanos, type(villanos) )