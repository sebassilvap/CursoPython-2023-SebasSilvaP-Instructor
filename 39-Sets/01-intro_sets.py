# =====================================================
# Sets

# - Colección de Conjuntos
# - Colección DESORDENADA y con elementos ÚNICOS
# - Elementos duplicados se eliminan automáticamente
# - No se puede cambiar sus elementos
# - Pero el set en si se puede cambiar / modificar
# - Se definen entre corchete => {}
# =====================================================


#? 1) Creación Básica de un set
print('\n1) Creación Básica de un set')
# - como el resto de colecciones
# - tienen len() para averiguar su tamaño
# - son desordenados
# - cuando imprimimos, no siguen el orden en el que fueron creados

conjunto = {'ecuador', 'usa', 'alemania', 'china'}

print(conjunto, type(conjunto) , len(conjunto))


#? 2) Creación de Set con la función set()
print('\n2) Creación de Set con la función set()')
# - más que función => constructor set()
# - al igual que listas y tuplas => puede almacenar diferentes tipos de datos

set_1 = {10, 'A', -5.5}
set_2 = set( (20, 'B', -10.9) )

# - dentro de set() => con paréntesis y valores

print( set_1, type(set_1), len(set_1) )
print( set_2, type(set_2), len(set_2) )


#? 3) Inicializar un set vacío
print('\n3) Inicializar un set vacío')
# - aunque no se puedan modificar los elementos de un set
# - veremos luego que el set tiene métodos
# - que permiten añadir elementos
# - por tanto podemos iniciar un set vacío

#! set_1 = {} # => de esta manera se crea un diccionario vacío, no set!!
set_1 = set()

print( set_1 , type(set_1) , len(set_1) )

# => intentando solo con llaves
set_2 = {}
print( set_2 , type(set_2) , len(set_2) )
# {} <class 'dict'> 0


#? 4) Set no permite elementos repetidos
print('\n3) Set no permite elementos repetidos')

set_1 = {'A', 100, 5.5, 'A', 10, 100}

print( set_1, len(set_1) )


#? 5) Indexing y Slicing
print('\n4) Indexing y Slicing')
# - Indexing & Slicing no es posible en set 
# - Resulta en TypeError

set_1 = { 10, 'python', -8.5, True }
#(+)       0     1        2     3
#(-)       4     3        2     1

print(set_1)
#
# print( set_1[0] ) #! TypeError: 'set' object is not subscriptable

#print( set_1[0:3] ) #! TypeError: 'set' object is not subscriptable


#? 6) in + set => averiguar si un elemento existe en el set
print('\n5) in + set => averiguar si un elemento existe en el set')

set_1 = { 10, 'python', -8.5, True }

print( 10 in set_1 ) # True
print( 'java' in set_1 ) # False


#? 7) Recorrido de set => manera de saber sus elementos
print('\n6) Recorrido de set => manera de saber sus elementos')
# - como vimos no es posible acceder a los items de un set con el index
# - pero es posible desplegar sus elementos
# - con un bucle

set_1 = { 10, 'python', -8.5, True }

for elemento in set_1:
    print(elemento)
# end for

# => si creamos elementos repetidos
# - la misma creación del set como vimos los filtra
# - y lo mismo vemos en el bucle

print()

set_1 = {'A', 100, 5.5, 'A', 10, 100}

for elemento in set_1:
    print(elemento)
# end for


#? 8) No existe concatenación ni producto en set
print('\n7) No existe concatenación ni producto en set')
# - Intentarlo nos lleva a un TypeError
# - Recordar que esto era muy válido en listas y tuplas

# 8.1) Recordar listas y tuplas:
print('\n7.1) Recordar listas y tuplas:\n')

lista_1 = [1,2,3]
lista_2 = ['A','B','C']

tupla_1 = (10,20,30)
tupla_2 = ('X', 'Y', 'Z')

# concatenación & producto
lista_concat = lista_1 + lista_2
lista_producto = 2 * lista_2

tupla_concat = tupla_1 + tupla_2
tupla_producto = 2 * tupla_2

# resultados
print( lista_concat, type(lista_concat), len(lista_concat) )
print( lista_producto, type(lista_producto), len(lista_producto) )
print( tupla_concat, type(tupla_concat), len(tupla_concat) )
print( tupla_producto, type(tupla_producto), len(tupla_producto) )

# 8.2) En set nos da error

set_1 = {'a', 'b', 'c'}
set_2 = {11, 12, 13}

#concat = set_1 + set_2
#! TypeError: unsupported operand type(s) for +: 'set' and 'set'

#prod = 2 * set_2
#! TypeError: unsupported operand type(s) for *: 'int' and 'set'