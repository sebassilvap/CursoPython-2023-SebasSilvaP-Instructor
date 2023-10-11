# =====================================
# Métodos Internos en Tuplas

# - Python ofrece 2 métodos internos
# - para trabajar con tuplas
#*  count()  &  index()
# =====================================

#? 1) .count()
print('\n1) .count()')
# - número de coincidencias
# - de un elemento dentro de una tupla

tupla = (10, 50, 'A', 10, '10', 'A', 'A')

print( tupla.count(10) )
print( tupla.count('A') )
print( tupla.count('10') ) # el tipo es importante
print( tupla.count('Z') ) # 0 => cuando cuento algo que no existe


#? 2) .index()
print('\n2) .index()')
# - devuelve el índice de coincidencia
# - de izquierda a derecha
# - si no existe da error

tupla = (10, 50, 'A', 10, '10', 'A', 'A')

print( tupla.index(10) )
print( tupla.index(50) )
print( tupla.index('A') )
#print( tupla.index('Z') ) #! ValueError: tuple.index(x): x not in tuple