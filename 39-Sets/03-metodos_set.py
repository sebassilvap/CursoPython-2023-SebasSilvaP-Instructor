# ==========================
# Métodos Internos para set
# ==========================


#? 1) .add()
print('\n1) .add()')
# - aunque no es posible cambiar los elementos
# - una vez creado el set
# - es posible añadir elementos

conjunto = {'A', 'B', 'C'}
print( conjunto, type(conjunto), len(conjunto) )

conjunto.add(10)
print( conjunto, type(conjunto), len(conjunto) )

conjunto.add(80)
print( conjunto, type(conjunto), len(conjunto) )

# => si intentamos añadir un elemento que ya existe
# - no pasa nada
# - recordar, que set no permite duplicados
conjunto.add('A')
print( conjunto, type(conjunto), len(conjunto) )



#? 2) .update()
print('\n2) .update()')
# - viene a ser como la concatenación entre sets
# - añade los elementos de 1 set a otro
# - modifica el set desde donde se lo aplica

colores_1 = { 'blanco', 'negro', 'gris' }
colores_2 = { 'azul', 'rojo', 'verde' }
colores_3 = { 'amarillo', 'azul', 'rojo' }

print( colores_1, type(colores_1), len(colores_1) )
print( colores_2, type(colores_2), len(colores_2) )
print( colores_3, type(colores_3), len(colores_3) )

colores_1.update(colores_2)

print('\n-----------------')
print( colores_1, type(colores_1), len(colores_1) )
print( colores_2, type(colores_2), len(colores_2) )
print( colores_3, type(colores_3), len(colores_3) )

# => los elementos que ya existen no se añaden
colores_2.update(colores_3)

print('\n-----------------')
print( colores_1, type(colores_1), len(colores_1) )
print( colores_2, type(colores_2), len(colores_2) )
print( colores_3, type(colores_3), len(colores_3) )



#? 3) .remove()
print('\n3) .remove()')
# - elimina un elemento del set
# - si el elemento que se manda a eliminar
# - NO existe
# - produce un error

colores = { 'amarillo', 'azul', 'rojo', 'blanco', 'negro' }
print( colores, type(colores), len(colores) )

colores.remove('rojo')
print( colores, type(colores), len(colores) )

# => eliminando algo que no existe
#colores.remove('verde') #! KeyError: 'verde'



#? 4) .discard()
print('\n4) .discard()')
# - igual que remove
# - pero no produce error
# - si trato de eliminar algo que no existe

colores = { 'amarillo', 'azul', 'rojo', 'blanco', 'negro' }
print( colores, type(colores), len(colores) )

colores.discard('rojo')
print( colores, type(colores), len(colores) )

# => eliminando algo que no existe
colores.discard('verde') # no pasa nada!
print( colores, type(colores), len(colores) )



#? 5) .pop()
print('\n5) .pop()')
# - al igual que en listas
# - eliminamos un elemento del set y lo retorna
# - pero como los set no tienen orden
# - se elimina un elemento al azar

heroes = { 'batman', 'superman', 'goku', 'ironman' }
print( heroes, type(heroes), len(heroes) )

heroes.pop()
print( heroes, type(heroes), len(heroes) )

# => elemento del pop, podemos guardarlo en una variable
heroe_eliminado = heroes.pop()

print( heroes, type(heroes), len(heroes) )
print( heroe_eliminado )


# => si seguimos eliminado hasta que no tenga elementos
# - vamos a tener un error
# - cuando no haya nada que eliminar

heroes.pop()
print( heroes, type(heroes), len(heroes) )

heroes.pop()
print( heroes, type(heroes), len(heroes) )

#heroes.pop() #! KeyError: 'pop from an empty set'



#? 6) .clear()
print('\n6) .clear()')
# - para dejar el set en blanco

colores = { 'amarillo', 'azul', 'rojo', 'blanco', 'negro' }
print( colores, type(colores), len(colores) )

colores.clear()
print( colores, type(colores), len(colores) )



#? 7) del
print('\n7) del')
# - elimina el set completamente
# - como variable incluso
# - después de esto ya no existe

colores = { 'amarillo', 'azul', 'rojo', 'blanco', 'negro' }
print( colores, type(colores), len(colores) )

del colores
#print( colores, type(colores), len(colores) )
#! NameError: name 'colores' is not defined.


# ---------------------------------
# * Métodos para ELIMINAR en sets
# .remove()
# .discard()
# .pop()
# .clear()
# del
# ---------------------------------


# ---------------------------
# * OPERACIONES DE CONJUNTOS
# ---------------------------

#? 8) .union()
print('\n8) .union()')
# - para crear un nuevo set
# - que une dos conjuntos
# - los duplicados son excluidos

set_1 = { 'A', 'R', 'T' }
set_2 = { 'X', 'Y', 'Z' }
set_3 = { 'S', 'T', 'A' }

union_1 = set_1.union(set_2)
union_2 = set_2.union(set_1)
union_3 = set_1.union(set_3)

print( union_1, len(union_1) )
print( union_2, len(union_2) )
print( union_3, len(union_3) )

print()
print( union_1 == union_2 ) # True
print( union_1 == union_3 ) # False

# => cuando tienen los mismos elementos
# - los set son iguales
# - no importa el desorden



#? 9) .intersection()
print('\n9) .intersection()')
# - para crear un nuevo set
# - que tenga los elementos en común entre 2 sets

set_1 = { 'A', 'R', 'T' }
set_2 = { 'X', 'Y', 'Z' }
set_3 = { 'S', 'T', 'A' }

# => no importa el orden, el resultado es el mismo
intersection_1 = set_1.intersection(set_3)
intersection_2 = set_3.intersection(set_1)

# => intersección entre 2 sets que no tienen nada en común
# - devuelve un set vacío
intersection_3 = set_1.intersection(set_2)

print( intersection_1, len(intersection_1) )
print( intersection_2, len(intersection_2) )
print( intersection_3, len(intersection_3) )



#? 10) .intersection_update()
print('\n10) .intersection_update()')
# - El mismo funcionamiento que .intersection()
# - Pero modifica al set donde se lo aplica

set_1 = { 'A', 'R', 'T' }
set_2 = { 'S', 'T', 'A' }

print( set_1, len(set_1) )
print( set_2, len(set_2) )

set_1.intersection_update(set_2)

print()
print( set_1, len(set_1) )
print( set_2, len(set_2) )



#? 11) .difference()
print('\n10) .difference()')

# *   set_1.difference(set_2)
# - devuelve un nuevo set
# - con los elementos que existen en set_1
# - pero no en set_2

set_1 = { 'P', 'Y', 'G', 'A', 'M', 'E' }
set_2 = { 'P', 'Y', 'T', 'O', 'N' }

difference_1 = set_1.difference(set_2)
difference_2 = set_2.difference(set_1)

print( difference_1, len(difference_1) )
print( difference_2, len(difference_2) )

print('\nSets Originales:')
print( set_1, len(set_1) )
print( set_2, len(set_2) )



#? 12) .difference_update()
print('\n12) .difference_update()')
# - funciona igual que .difference()
# - pero modifica al set donde se lo aplica

set_1 = { 'P', 'Y', 'G', 'A', 'M', 'E' }
set_2 = { 'P', 'Y', 'T', 'O', 'N' }

print( set_1, len(set_1) )
print( set_2, len(set_2) )

set_1.difference_update(set_2)

print()
print( set_1, len(set_1) )
print( set_2, len(set_2) )



#? 13) .symmetric_difference()
print('\n13) .symmetric_difference()')

set_1 = { 'P', 'Y', 'G', 'A', 'M', 'E' }
set_2 = { 'P', 'Y', 'T', 'O', 'N' }

print( set_1, len(set_1) )
print( set_2, len(set_2) )

# .difference()
# - en este caso devuelve G, A, M, E
print('\n.difference()\n')

diff = set_1.difference(set_2)
print( diff, len(diff) )

# .symmetric_difference()
# - en este caso devuelve G, A, M, E y también T, O, N
# - es decir todo menos lo que coincide
print('\n.symmetric_difference()\n')

symmetric_diff = set_1.symmetric_difference(set_2)
print( symmetric_diff, len(symmetric_diff) )



#? 14) .symmetric_difference_update()
print('\n14) .symmetric_difference_update()')
# - funciona igual que .symmetric_difference
# - pero modifica la variable donde se lo usa

set_1 = { 'P', 'Y', 'G', 'A', 'M', 'E' }
set_2 = { 'P', 'Y', 'T', 'O', 'N' }

print( set_1, len(set_1) )
print( set_2, len(set_2) )

set_1.symmetric_difference_update(set_2)

print()
print( set_1, len(set_1) )
print( set_2, len(set_2) )


# -----------------------------------------
# * NOTA
# - todos los que tienen el "_update"
# - modifican el set donde se les aplica
# -----------------------------------------



# -------------------------------
# * MÉTODOS BOOLEANOS
# - devuelven True o False
# - dependiendo del método
# - y lo que queramos averiguar
# -------------------------------


#? 15) .isdisjoint()
print('\n15) .isdisjoint()')
# - devuelve True
# - si 2 conjuntos NO tienen una intersección
# - intersección => elementos en común

heroes_1 = { 'goku', 'superman', 'batman' }
heroes_2 = { 'hulk', 'ironman', 'goku' }
heroes_3 = { 'hulk', 'ironman', 'spiderman' }

# Recordar intersection
print('\nRecordar intersection\n')

intersection_1 = heroes_1.intersection(heroes_2)
intersection_2 = heroes_1.intersection(heroes_3)

print( intersection_1 )
print( intersection_2 )

# aplicando .isdisjoint()
print('\naplicando .isdisjoint()\n')

print( heroes_1.isdisjoint(heroes_2) )
print( heroes_2.isdisjoint(heroes_1) )
print( heroes_1.isdisjoint(heroes_3) )



#? 16) .issubset()
print('\n16) .issubset()')
# - Retorna True
# - Si un set está contenido en otro

numeros_1 = {1,2,3,4,5}
numeros_2 = {1,2,3}
numeros_3 = {1,2,3,10}

print( numeros_1.issubset(numeros_2) )
print( numeros_2.issubset(numeros_1) ) # True
print( numeros_3.issubset(numeros_1) )



#? 17) .issuperset()
print('\n17) .issuperset()')
# - Retorna True
# - Si un set contiene a otro

numeros_1 = {1,2,3,4,5}
numeros_2 = {1,2,3}
numeros_3 = {1,2,3,10}

print( numeros_1.issuperset(numeros_2) ) # True
print( numeros_2.issuperset(numeros_1) )
print( numeros_3.issuperset(numeros_1) )