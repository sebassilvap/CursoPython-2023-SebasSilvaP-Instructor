# =================================
# Listas - Completo

# => Indexing & Slicing
# =================================


#? 1) Indexing
print('\n1) Indexing')
# - Acceder a los subelementos
# - de elementos iterables
# - por medio de su index / posición

lista = [100,200,300,400,500]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

# acceder al último con índice negativo
print(lista[-1])



#? 2) Slicing
print('\n2) Slicing')
# - técnica para acceder a una sublista
# - de una lista dada
# - recordar que el end es exclusivo
# *      [start : end : step]


letras = ['a','b','c','d','e','f','g','h']
#          0   1   2   3   4   5   6   7

print(letras, type(letras), len(letras))

print( letras[0:4] )
print( letras[3:8] )
print('------')
print( letras[:4] )
print( letras[3:] )
print('------')
print( letras[1:7:2] )
print('------')
# => para saltar todo
print( letras[::1] )
print( letras[::2] ) # salta 2
print( letras[::3] ) # salta 3
print('------')
# => dato curioso
print( letras[::] ) # sin especificar start, end y step
print(letras)



#? 3) IndexError
print('\n3) IndexError')
# - se produce en el indexing
# - más no en el slicing

lista = [1,2,3,4,5]
# (+)    0 1 2 3 4
# (-)    5 4 3 2 1

# EJ: en slicing
print( lista[2:100] )

# EJ: en indexing
#print( lista[100] ) #! IndexError: list index out of range

#print( lista[-6] ) #! IndexError: list index out of range