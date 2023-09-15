# ===========================================================================
# Índices de un String

# - los string son elementos ITERABLES
# - ya veremos luego en qué consiste esta palabra ITERABLE
# - y qué implica
# - pero por el momento es importante saber que este tipo de elementos
# - manejan un índice => que marca la posición de cada componente
# - en programación en general cuando se habla de índices
# - estos empiezan desde el 0
# - y el índice -1 se refiere a la última posición
# ===========================================================================

#? 1) Recorrer string con índices POSITIVOS

l   =  'juan'
# (+)   0123
# (-)   4321

print(l)

print('(1) Índices (+)\n-----------')
print(l[0])
print(l[1])
print(l[2])
print(l[3])

#? 2) Recorrer string con índices NEGATIVOS

print('\n(2) Índices (-)\n-----------')
print(l[-1])
print(l[-2])
print(l[-3])
print(l[-4])

#? 3) Utilizando cada índice

print('\n(3) Utilizando cada índice')
print( l[0] + l[1] + l[2] + l[3] )
print( l[1] + l[3] + l[0] + l[2] )
print( l[1] + l[1] + l[2] + l[2] + l[-3] )

print( l , type(l) )
print( l[0] , type(l[0]) )
print( l[1] , type(l[1]) )
print( l[2] , type(l[2]) )
print( l[3] , type(l[3]) )

#? 4) Intentando acceder a un string que no existe
# - Index Error => cuando intento acceder a un índice fuera de los límites

#print( l[4] ) #! Index Error
#print( l[-5] ) #! Index Error