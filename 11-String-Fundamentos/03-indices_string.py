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
print('\n1) Recorrer string con índices POSITIVOS')

var   =  'juan'
#(+)      0123
#(-)      4321

print(var)

print()

print(var[0])
print(var[1])
print(var[2])
print(var[3])



#? 2) Recorrer string con índices NEGATIVOS
print('\n2) Recorrer string con índices NEGATIVOS')

print(var[-1])
print(var[-2])
print(var[-3])
print(var[-4])



#? 3) Utilizando cada índice
print('\n3) Utilizando cada índice')

print( var[0] + var[1] + var[2] + var[3] )
print( var[1] + var[3] + var[0] + var[2] )
print( var[1] + var[1] + var[2] + var[2] + var[-3] )

print( var , type(var) )
print( var[0] , type(var[0]) )
print( var[1] , type(var[1]) )
print( var[2] , type(var[2]) )
print( var[3] , type(var[3]) )



#? 4) Intentando acceder a un string que no existe
print('\n4) Intentando acceder a un string que no existe')
# - Index Error => cuando intento acceder a un índice fuera de los límites

#print( l[4] ) #! Index Error
#print( l[-5] ) #! Index Error