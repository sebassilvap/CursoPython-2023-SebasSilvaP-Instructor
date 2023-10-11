# ========================================================
# Tuplas

# - Colecciones igual a las listas
# - Con la característica de ser INMUTABLES
# - Recordar: Las listas son MUTABLES
# - Nos aseguran que sus datos no se pueden modificar
# - Listas: se declaran con []
# - Tuplas: se declaran con ()
# ========================================================


#? 1) Creación de una tupla
print('\n1) Creación de una tupla')
# - dos maneras
# - directamente con los datos en () separados con ,
# - utilizando la función tuple() => que de manera formal recibe el nombre de constructor

tupla_1 = (500, 'python', -8.9, True)

tupla_2 = tuple( (100, 'java', -5.5, False) )

print( tupla_1 , type(tupla_1) )
print( tupla_2 , type(tupla_2) )


#? 2) Indexing & Slicing en Tuplas
print('\n2) Indexing & Slicing en Tuplas')

tupla_1 = ('a', 'b', 'c', 'd', 'e', 'f')
#(+)        0    1    2    3    4    5
#(-)        6    5    4    3    2    1

# => Indexing
print( tupla_1, type(tupla_1) )
print( tupla_1[0] )
print( tupla_1[4] )
print( tupla_1[-1] ) # index -1 último elemento
print( tupla_1[-6] )
#print( tupla_1[8] ) #! IndexError: tuple index out of range

# => Slicing
print( tupla_1[0:3] )
print( tupla_1[3:6] )
print( tupla_1[-5:-1] )
print( tupla_1[:4] )
print( tupla_1[2:] )
print( tupla_1[::2] )
print( tupla_1[2:100] ) # recordar que en slicing no tenemos IndexError


#? 3) función len()
print('\n3) función len()')
# - al igual que en string y listas
# - devuelve el tamaño de una tupla

tupla_1 = ('a', 'b', 'c', 'd', 'e', 'f')
tupla_2 = tuple( (100, 'java', -5.5, False) )

print( tupla_1 , len(tupla_1) )
print( tupla_2 , len(tupla_2) )


#? 4) in + tuplas
print('\n4)in + tuplas')
# - una manera de averiguar si un elemento está en la tupla

tupla_1 = (500, 'python', -8.9, True)

print( 200 in tupla_1 )
print( 'java' in tupla_1 )
print( 'python' in tupla_1 )


#? 5) Las Tuplas son INMUTABLES
print('\n5) Las Tuplas son INMUTABLES')
# - la única manera de cambiarlas es reasignando
# - pero no existe manera de modificarlas

tupla_1 = (500, 'python', -8.9, True)
print(tupla_1, type(tupla_1))

#tupla_1[0] = -100 #! TypeError: 'tuple' object does not support item assignment

# 5.1) Concatenando Valores
print('\n5.1) Concatenando Valores\n')

tupla_1 = (500, 'python', -8.9, True)
tupla_2 = ('A', 'B')
print(tupla_1)
print(tupla_2)

tupla_1 = tupla_1 + tupla_2
print(tupla_1)

# => shortcut de incremento
# concatenación en la asignación
tupla_1 = (500, 'python', -8.9, True)
tupla_2 = ('A', 'B')

tupla_1 += tupla_2
print(tupla_1)


# 5.2) Concatenando 1 valor
print('\n5.2) Concatenando 1 valor\n')

tupla_1 = (500, 'python', -8.9, True)
tupla_2 = (1000,) #! para evitar error se deja la coma al final

print( tupla_1, type(tupla_1), len(tupla_1) )
print( tupla_2, type(tupla_2), len(tupla_2) )

tupla_1 += tupla_2
print( tupla_1, type(tupla_1), len(tupla_1) )


# 5.3) Casting a Lista para modificación
print('\n5.3) Casting a Lista para modificación\n')

tupla_1 = (500, 'python', -8.9, True)

lista_1 = list(tupla_1)

print( tupla_1, type(tupla_1), len(tupla_1) )
print( lista_1, type(lista_1), len(lista_1) )

lista_1.append('A')

tupla_1 = tuple(lista_1)

print( tupla_1, type(tupla_1), len(tupla_1) )