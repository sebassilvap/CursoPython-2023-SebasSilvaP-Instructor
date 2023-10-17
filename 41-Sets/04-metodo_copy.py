# =======================================================
# Método .copy() en sets

# - devuelve una copia del set
# - el mismo problema que en listas
# - cuando se crea un set igual directamente a otro set
# =======================================================


#? 1) Problema al crear un set igual a otro set
print('\n1) Problema al crear un set igual a otro set')

set_1 = { 'A', 'B', 'C' }

set_2 = set_1

print( set_1, len(set_1) )
print( set_2, len(set_2) )

# => modificando set_1
set_1.add(100)

print()
print( set_1, len(set_1) )
print( set_2, len(set_2) )

# => modificando set_2
set_2.add('PYTHON')

print()
print( set_1, len(set_1) )
print( set_2, len(set_2) )

# - recordemos que al crear de esta manera
# - ambas variables apuntan a la misma dirección de la memoria
# - este problema pasaba igual con las listas
# - la solución era con .copy()



#? 2) Solución al problema utilizando .copy()
print('\n2) Solución al problema utilizando .copy()')

set_1 = { 'A', 'B', 'C' }

set_2 = set_1.copy()

print( set_1, len(set_1) )
print( set_2, len(set_2) )

# => modificando set_1
set_1.add(100)

print()
print( set_1, len(set_1) )
print( set_2, len(set_2) )

# => modificando set_2
set_2.add('PYTHON')

print()
print( set_1, len(set_1) )
print( set_2, len(set_2) )