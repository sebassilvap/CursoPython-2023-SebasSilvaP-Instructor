# ===============================================================================
# Usando while para iterar secuencias de datos

# - aunque el bucle por excelencia para iterar secuencias en python es el => for
# - también podemos usar while usando un contador externo
#!  las secuencias son aquellas a las cuales podemos acceder con sus índices

# - por el momento hemos visto 3 secuencias: string, lista, range
# ===============================================================================


#? 1) while iterando string
print('\n1) while iterando string')

cadena = 'python'
#         012345

print( cadena, type(cadena) )
print( 'cadena[0] =' , cadena[0] )
print( 'cadena[1] =' , cadena[1] )
print( 'cadena[2] =' , cadena[2] )
print( 'cadena[3] =' , cadena[3] )
print( 'cadena[4] =' , cadena[4] )
print( 'cadena[5] =' , cadena[5] )

# => utilizando while + contador
print()

index = 0

while index < len(cadena): 
    print( 'cadena[' + str(index) + '] =' , cadena[index] )
    index += 1
# end while

#! importante fijar correctamente la condición del while
#! de otra manera caemos en un index error

# ej:

'''
print()

index = 0

while index <= len(cadena): 
    print( 'cadena[' + str(index) + '] =' , cadena[index] )
    index += 1
# end while
'''
#! IndexError: string index out of range



#? 2) while iterando listas
print('\n2) while iterando listas')

frutas = ['manzana','piña','durazno','uvas','banana']
#             0        1       2       3       4

# => accediendo de la manera que hemos aprendido a los elementos
print(frutas, '|', type(frutas) , '|', len(frutas))
print( 'frutas[0] =' , frutas[0] )
print( 'frutas[1] =' , frutas[1] )
print( 'frutas[2] =' , frutas[2] )
print( 'frutas[3] =' , frutas[3] )
print( 'frutas[4] =' , frutas[4] )

# => utilizando while + index
print()

index = 0

while index < len(frutas):
    print( 'frutas[' + str(index) + '] =', frutas[index] )
    index += 1
# end while

#! Tener cuidado con el Indexerror

'''
print()

index = 0

while index <= len(frutas):
    print( 'frutas[' + str(index) + '] =', frutas[index] )
    index += 1
# end while
'''
#! IndexError: list index out of range



#? 3) while iterando range
print('\n3) while iterando range')

# => recordar rango 
rango_1_5 = range(1,6)
print( rango_1_5, '|', type(rango_1_5), '|', len(rango_1_5) )
print( 'rango_1_5[0] = ' , rango_1_5[0] )
print( 'rango_1_5[1] = ' , rango_1_5[1] )
print( 'rango_1_5[2] = ' , rango_1_5[2] )
print( 'rango_1_5[3] = ' , rango_1_5[3] )
print( 'rango_1_5[4] = ' , rango_1_5[4] )
#print( 'rango_1_5[5] = ' , rango_1_5[5] ) #! IndexError: range object index out of range

# => utilizando while + index
print()
index = 0

while index < len(rango_1_5):
    print( 'rango_1_5[' + str(index) + '] =', rango_1_5[index] )
    index += 1
# end while